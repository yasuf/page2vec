from chromadb import CloudClient

async def upload_file_to_chromadb(file=None, api_key=None, database_name=None, tenant_id=None):
    client = CloudClient(api_key=api_key, tenant=tenant_id, database=database_name)
    collection = client.get_or_create_collection(database_name)

    print(f"⏳ Starting: Uploading records to ChromaDB..")

    lines = []
    for line in file.readlines():
        lines.append(line)

    collection.add(
        documents=lines,
        ids=[f"id{i}" for i in range(len(lines))]
    )

    print(f"✅ Completed: Uploaded {len(lines)} records to ChromaDB")
