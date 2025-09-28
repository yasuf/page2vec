from chromadb import CloudClient

async def upload_file_to_chromadb(file=None, api_key=None, collection_name=None):
    client = CloudClient(api_key=api_key)
    collection = await client.create_collection(collection_name)

    print(f"⏳ Starting: Uploading records to ChromaDB..")

    file_lines_length = len(file.readlines())

    await collection.add(
        documents=file.readlines(),
        ids=[f"id{i}" for i in range(file_lines_length)]
    )

    print(f"✅ Completed: Uploaded {file_lines_length} records to ChromaDB")
