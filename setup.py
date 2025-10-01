"""Setup script for page2vec package."""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements from Pipfile (convert to requirements.txt format)
def read_requirements():
    """Extract requirements from Pipfile."""
    requirements = [
        "browser-use>=0.3.0",
        "pinecone>=2.2.0",
        "chromadb>=1.1.0",
        "pymilvus>=2.2.0",
        "milvus-model",
        "python-dotenv"
    ]
    return requirements

setup(
    name="page2vec",
    version="0.1.0",
    author="Yasu",
    author_email="",  # Add your email if desired
    description="Convert knowledge base websites into vectors for vector databases",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/page2vec",  # Update with actual repo URL
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest",
            "pytest-asyncio",
            "black",
            "flake8",
            "mypy",
        ],
    },
    entry_points={
        "console_scripts": [
            "page2vec=page2vec.core:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="vector database, embeddings, web scraping, knowledge base, pinecone, chromadb, milvus",
)
