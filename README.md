## Description

Convert your knowledge base website into a text file that you can store as a vector in any of the existing vector databases.

The databases supported are:

* Pinecone
* ChromaDB (Coming soon)

## Example Usage

**Pinecone**

Update all values with the ones from your account, API key, index name and namespace.

```
python page2vec.py \
  --database pinecone \
  --url "[INSERT A URL]"  \
  --pinecone-api-key "[YOUR API KEY]"  \
  --pinecone-index "page2vec-testing" \
  --pinecone-namespace "page2vec-default"
```

**ChromaDB**

```
python page2vec.py \
  --url "[INSERT A URL]"  \
  --database chromadb \
  --chromadb-api-key "[YOUR API KEY]"  \
  --chromadb-collection "page2vec-testing"
```

**Milvus**
```
python page2vec.py \
  --url "[INSERT A URL]"  \
  --database milvus \
  --milvus-otuput-file "[YOUR API KEY]"  \
  --milvus-collection "page2vec-testing"
```
```


## Dependencies

This project uses browser-use


# Notes:

These databases will be supported in the future (or upon request):

* PostgreSQL
* Elasticsearch
