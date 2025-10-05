## Description

Convert your knowledge base website (or any page) into a text file that you can store as a vector in any of the existing vector databases. Uses AI browser automation to scrape and process web content.

The databases supported are:

* Pinecone
* ChromaDB
* Milvus

## Installation

```bash
pip install page2vec
```

## Example Usage

### Command Line Interface

After installation, you can use the `page2vec` command. All commands require an OpenAI API key for the LLM that browser automation agent uses.

**Pinecone**

Update all values with the ones from your account: API key, index name, namespace, etc.

```bash
page2vec \
  --database pinecone \
  --url "[INSERT A URL]"  \
  --openai-api-key "[YOUR OPENAI API KEY]"  \
  --pinecone-api-key "[YOUR PINECONE API KEY]"  \
  --pinecone-index "page2vec-testing" \
  --pinecone-namespace "page2vec-default"
```

**ChromaDB**

```bash
page2vec \
  --url "[INSERT A URL]"  \
  --database chromadb \
  --openai-api-key "[YOUR OPENAI API KEY]"  \
  --chromadb-api-key "[YOUR CHROMADB API KEY]"  \
  --chromadb-database-name "page2vec-testing"
```

**Milvus**
```bash
page2vec \
  --url "[INSERT A URL]"  \
  --database milvus \
  --openai-api-key "[YOUR OPENAI API KEY]"  \
  --milvus-output-file "milvus_data.db"  \
  --milvus-collection-name "page2vec-testing"
```

## Custom prompt example

page2vec \
  --database pinecone \
  --url "[INSERT A URL]"  \
  --openai-api-key "[YOUR OPENAI API KEY]"  \
  --pinecone-api-key "[YOUR PINECONE API KEY]"  \
  --pinecone-index "page2vec-testing" \
  --pinecone-namespace "page2vec-default"
  --custom-prompt "Find all the paragraphs of the documentation in https://docs.trychroma.com/docs/overview/contributing. Store only the first 3 paragraphs in a separate row in a CSV."

### Python API

You can also use page2vec programmatically:

```python
import asyncio
from page2vec import async_main
from argparse import Namespace

# Create arguments
args = Namespace(
    database="pinecone",
    url="https://docs.example.com",
    openai_api_key="your-openai-api-key",
    pinecone_api_key="your-pinecone-api-key",
    pinecone_index="your-index",
    pinecone_namespace="your-namespace",
    test_mode=False
)

# Run the process
asyncio.run(async_main(args))
```

## Dependencies

This project uses:
- **browser-use**: AI-powered browser automation for intelligent web scraping
- Database SDKs: Pinecone, ChromaDB, and Milvus clients

## Future Support

These databases will be supported in the future (or upon request):
- PostgreSQL
- Elasticsearch


### Development Installation
If you'd like to debug something or contribute:

```bash
git clone <repository-url>
cd page2vec
pip install -e ".[dev]"
```
