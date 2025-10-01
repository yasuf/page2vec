"""Test basic imports and package structure."""

import pytest


def test_package_import():
    """Test that the package can be imported."""
    import page2vec
    assert page2vec.__version__ == "0.1.0"


def test_main_function_import():
    """Test that main functions can be imported."""
    from page2vec import main, async_main
    assert callable(main)
    assert callable(async_main)


def test_database_helpers_import():
    """Test that database helper functions can be imported."""
    from page2vec import (
        upload_file_to_pinecone,
        upload_file_to_chromadb,
        upload_file_to_milvus
    )
    assert callable(upload_file_to_pinecone)
    assert callable(upload_file_to_chromadb)
    assert callable(upload_file_to_milvus)


def test_core_module_import():
    """Test that core module can be imported."""
    from page2vec.core import create_parser, SUPPORTED_DATABASES
    assert callable(create_parser)
    assert isinstance(SUPPORTED_DATABASES, list)
    assert "pinecone" in SUPPORTED_DATABASES
    assert "chromadb" in SUPPORTED_DATABASES
    assert "milvus" in SUPPORTED_DATABASES
