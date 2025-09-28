import argparse
from pinecone import Pinecone

parser = argparse.ArgumentParser(description="A script to convert a knowledge base into vectors and store them in a database.")
parser.add_argument("--database", type=str, help="The database to store the vectors in.", default="pinecone")
parser.add_argument("--pinecone-api-key", type=str, help="The API key of the Pinecone database.", default="")
parser.add_argument("--pinecone-index", type=str, help="The index to store the vectors in.", default="")
parser.add_argument("--pinecone-namespace", type=str, help="The namespace to store the vectors in.", default="")
args = parser.parse_args()

pinecone_api_key = args.pinecone_api_key
pinecone_index = args.pinecone_index
pinecone_namespace = args.pinecone_namespace

pc = Pinecone(api_key=pinecone_api_key)

def upload_file_to_pinecone(file):
    dense_index = pc.Index(pinecone_index)

    records_batches = {}

    i = 0
    batch = 0

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
