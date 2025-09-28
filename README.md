## Description

Convert your knowledge base into a large text file that you can store as a vector in any of the existing vector databases.

The databases supported are:

* ChromaDB

* Pinecone

## Example Usage

**Pinecone**

```
python know2vec.py "https://yourknowledgebasesite.com" --database pinecone --key [MY KEY] --index [INDEX NAME]

> Created file in `knowledgebase_1.csv"
```

**ChromaDB**

```
python know2vec.py "https://yourknowledgebase.com" --database chromadb --key [MY KEY] --index [INDEX NAME]

> Created file in `knowledgebase_1.csv"
```


## Dependencies

This project uses browser-use



# Notes:

These databases will be supported in the future (or upon request):

* PostgreSQL

* Elasticsearch
