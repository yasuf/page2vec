from chromadb import CloudClient

async def upload_file_to_chromadb(file=None, api_key=None, database_name=None, tenant_id=None):
    client = CloudClient(api_key=api_key, tenant=tenant_id, database=database_name)
    collection = await client.create_collection(database_name)

    print(f"⏳ Starting: Uploading records to ChromaDB..")

    file_lines_length = len(file.readlines())

    await collection.add(
        documents=file.readlines(),
        ids=[f"id{i}" for i in range(file_lines_length)]
    )

    print(f"✅ Completed: Uploaded {file_lines_length} records to ChromaDB")
