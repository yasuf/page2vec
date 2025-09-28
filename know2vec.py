## TODO:
# 2. Let the user enter more than 1 URL, they can enter a list of URLS and the agent or agents should go through them all
#   so we create a full knowledge base.

from browser_use import Agent, ChatOpenAI, Browser
from dotenv import load_dotenv
import argparse
from pinecone_helper import upload_file_to_pinecone
load_dotenv()

supported_databases = ["pinecone"]

browser = Browser(headless=True)

parser = argparse.ArgumentParser(description="A script to convert a knowledge base into vectors and store them in a database.")
parser.add_argument("--database", type=str, help="The database to store the vectors in.", default="pinecone")
parser.add_argument("--pinecone-api-key", type=str, help="The API key of the Pinecone database.", default="")
parser.add_argument("--pinecone-index", type=str, help="The index to store the vectors in.", default="")
parser.add_argument("--pinecone-namespace", type=str, help="The namespace to store the vectors in.", default="")
args = parser.parse_args()

database = args.database
pinecone_api_key = args.pinecone_api_key
pinecone_index = args.pinecone_index
pinecone_namespace = args.pinecone_namespace

if database not in supported_databases:
  print(f"Database {database} not supported")
  exit(1)

prompt = """
  Find the first 2 paragraphs of the documentation in https://developer.fountain.com/reference/overview.

  Store each paragraph in a separate row in a CSV.
"""

agent = Agent(
    task=prompt,
    llm=ChatOpenAI(model="o4-mini"),
    browser=browser,
)
history = agent.run_sync()
action_results = history.action_results()

print("Done with the Agent, starting to upload data to vector storage")

files = []

for result in action_results:
  if result.attachments is not None:
    for attachment in result.attachments:
      files.append(attachment)
      print(f"Added file to array: {attachment}")

# Upload files to vector storage
for file in files:
  with open(file, "r") as f:
    if database == "pinecone":
      upload_file_to_pinecone(file=f,
        pinecone_api_key=pinecone_api_key,
        pinecone_index=pinecone_index,
        pinecone_namespace=pinecone_namespace
      )
    else:
      print(f"Database {database} not supported")
