from pymilvus import MilvusClient, model

def upload_file_to_milvus(file=None, milvus_collection_name=None, milvus_output_file=None):
  print(f"⏳ Starting: Uploading records to Milvus..")

  client = MilvusClient(milvus_output_file)

  if client.has_collection(collection_name=milvus_collection_name):
    client.drop_collection(collection_name=milvus_collection_name)

  client.create_collection(
    collection_name=milvus_collection_name,
    # The vectors we will use in this demo has 768 dimensions
    dimension=768,
  )

  embedding_fn = model.DefaultEmbeddingFunction()

  docs = file.readlines()
  vectors = embedding_fn.encode_documents(docs)

  print("Dim:", embedding_fn.dim, vectors[0].shape)  # Dim: 768 (768,)

  data = [
      {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"}
      for i in range(len(vectors))
  ]

  print("Data has", len(data), "entities, each with fields: ", data[0].keys())
  print("Vector dim:", len(data[0]["vector"]))

  res = client.insert(collection_name=milvus_collection_name, data=data)

  print(res)
  print(f"✅ Completed: Uploaded {len(data)} records to Milvus")
