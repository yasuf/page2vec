"""
page2vec - Convert knowledge base websites into vectors for storage in vector databases.

This package provides functionality to scrape documentation websites and convert
the content into vector embeddings that can be stored in various vector databases
including Pinecone, ChromaDB, and Milvus.
"""

__version__ = "0.1.0"
__author__ = "Yasu"
__description__ = "Convert knowledge base websites into vectors for vector databases"

from .core import main, async_main
from .database_helpers import (
    upload_file_to_pinecone,
    upload_file_to_chromadb,
    upload_file_to_milvus
)

__all__ = [
    "main",
    "async_main",
    "upload_file_to_pinecone",
    "upload_file_to_chromadb",
    "upload_file_to_milvus"
]
