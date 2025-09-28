from pinecone import Pinecone

def upload_file_to_pinecone(file=None, pinecone_api_key=None, pinecone_index=None, pinecone_namespace=None):
    pc = Pinecone(api_key=pinecone_api_key)
    dense_index = pc.Index(pinecone_index)

    records_batches = {}

    i = 0
    batch = 0

    print(f"⏳ Starting: Uploading records to Pinecone..")

    for line in file.readlines():
      if i % 50 == 0 and i != 0:
        batch += 1
      records_batches.setdefault(batch, [])
      i += 1
      records_batches[batch].append({
        "_id": f"rec{i}",
        "text": line
      })

    for _, batch_data in records_batches.items():
      dense_index.upsert_records(pinecone_namespace, batch_data)

    print(f"✅ Completed: Uploaded {i} records to Pinecone")
