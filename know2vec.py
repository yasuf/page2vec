## TODO:
# 1. From the agent's history, retrieve the file's path and copy it into this repository for easy access.
# 2. Let the user enter more than 1 URL, they can enter a list of URLS and the agent or agents should go through them all
#   so we create a full knowledge base.


from browser_use import Agent, ChatOpenAI, Browser
from dotenv import load_dotenv
load_dotenv()

browser = Browser(headless=True)

prompt = """
  Find the full main text of the documentation of https://developer.fountain.com/reference/overview.

  Store each paragraph in a separate row in a CSV.
"""

agent = Agent(
    task=prompt,
    llm=ChatOpenAI(model="o4-mini"),
    browser=browser,  # Uses Browser-Use cloud for the browser
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
    for line in f.readlines():
      # upload to vector storage
      print("Uploading to vector storage: ", line)
      pass
