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

  Store it in this repository as a file called `knowledgebase_1.csv` within the outputs directory.
"""

agent = Agent(
    task=prompt,
    llm=ChatOpenAI(model="o4-mini"),
    browser=browser,  # Uses Browser-Use cloud for the browser
)
agent.run_sync()


