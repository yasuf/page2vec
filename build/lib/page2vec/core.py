"""
Core functionality for page2vec package.

This module contains the main logic for scraping websites and converting
content to vectors for storage in vector databases.
"""

from browser_use import Agent, ChatOpenAI, Browser
from dotenv import load_dotenv
import argparse
import asyncio

import nest_asyncio
nest_asyncio.apply()

import sys

from .database_helpers import (
    upload_file_to_pinecone,
    upload_file_to_chromadb,
    upload_file_to_milvus
)

load_dotenv()

SUPPORTED_DATABASES = ["pinecone", "chromadb", "milvus"]


def create_parser():
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="A script to convert a knowledge base into vectors and store them in a database."
    )

    # Main arguments
    parser.add_argument(
        "--database",
        type=str,
        help="The database to store the vectors in.",
        default="pinecone",
        choices=SUPPORTED_DATABASES
    )
    parser.add_argument(
        "--url",
        type=str,
        help="The URL to scrape.",
        default="https://docs.github.com/en/rest/about-the-rest-api/about-the-openapi-description-for-the-rest-api?apiVersion=2022-11-28"
    )

    # Pinecone specific arguments
    parser.add_argument(
        "--pinecone-api-key",
        type=str,
        help="The API key of the Pinecone database.",
        default=""
    )
    parser.add_argument(
        "--pinecone-index",
        type=str,
        help="The index to store the vectors in.",
        default=""
    )
    parser.add_argument(
        "--pinecone-namespace",
        type=str,
        help="The namespace to store the vectors in.",
        default=""
    )

    # ChromaDB specific arguments
    parser.add_argument(
        "--chromadb-api-key",
        type=str,
        help="The API key of the ChromaDB database.",
        default=""
    )
    parser.add_argument(
        "--chromadb-tenant-id",
        type=str,
        help="The tenant ID of the ChromaDB database.",
        default=""
    )
    parser.add_argument(
        "--chromadb-database-name",
        type=str,
        help="The name of the collection to store the vectors in.",
        default=""
    )

    # Milvus specific arguments
    parser.add_argument(
        "--milvus-output-file",
        type=str,
        help="The name of the file to store the vectors in.",
        default=""
    )
    parser.add_argument(
        "--milvus-collection-name",
        type=str,
        help="The name of the collection to store the vectors in.",
        default=""
    )

    # Test mode, shorter agent cycle
    parser.add_argument(
        "--test-mode",
        action="store_true",
        help="If true, the agent will only look for the first 2 paragraphs.",
        default=False
    )

    return parser


async def scrape_website(url: str, test_mode: bool = False, openai_api_key: str = "") -> list:
    """
    Scrape a website and extract paragraphs using browser automation.

    Args:
        url: The URL to scrape
        test_mode: If True, only extract first 2 paragraphs

    Returns:
        List of file paths containing the scraped content
    """
    browser = Browser(headless=True)

    if test_mode:
        prompt = f"""
        Find the first 2 paragraphs of the documentation in {url}.
        Store each paragraph in a separate row in a CSV.
        """
    else:
        prompt = f"""
        Find all the paragraphs of the documentation in {url}.
        Store each paragraph in a separate row in a CSV.
        """

    agent = Agent(
        task=prompt,
        llm=ChatOpenAI(model="o4-mini", api_key=openai_api_key),
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

    return files


async def upload_files_to_vector_storage(files: list, database: str, **kwargs):
    """
    Upload files to the specified vector storage database.

    Args:
        files: List of file paths to upload
        database: Database type ('pinecone', 'chromadb', 'milvus')
        **kwargs: Database-specific configuration parameters
    """
    for file_path in files:
        with open(file_path, "r") as f:
            if database == "pinecone":
                upload_file_to_pinecone(
                    file=f,
                    pinecone_api_key=kwargs.get('pinecone_api_key'),
                    pinecone_index=kwargs.get('pinecone_index'),
                    pinecone_namespace=kwargs.get('pinecone_namespace')
                )
            elif database == "chromadb":
                await upload_file_to_chromadb(
                    file=f,
                    api_key=kwargs.get('chromadb_api_key'),
                    database_name=kwargs.get('chromadb_database_name'),
                    tenant_id=kwargs.get('chromadb_tenant_id'),
                )
            elif database == "milvus":
                await upload_file_to_milvus(
                    file=f,
                    output_file=kwargs.get('milvus_output_file'),
                    collection_name=kwargs.get('milvus_collection_name'),
                )
            else:
                print(f"Database {database} not supported")


async def async_main(args):
    """Main async function that orchestrates the entire process."""
    # Validate database choice
    if args.database not in SUPPORTED_DATABASES:
        print(f"Database {args.database} not supported")
        sys.exit(1)

    # Scrape the website
    files = await scrape_website(args.url, args.test_mode, args.openai_api_key)

    if not files:
        print("No files were generated from the scraping process")
        return

    # Prepare database-specific parameters
    db_params = {}
    if args.database == "pinecone":
        db_params.update({
            'pinecone_api_key': args.pinecone_api_key,
            'pinecone_index': args.pinecone_index,
            'pinecone_namespace': args.pinecone_namespace
        })
    elif args.database == "chromadb":
        db_params.update({
            'chromadb_api_key': args.chromadb_api_key,
            'chromadb_database_name': args.chromadb_database_name,
            'chromadb_tenant_id': args.chromadb_tenant_id
        })
    elif args.database == "milvus":
        db_params.update({
            'milvus_output_file': args.milvus_output_file,
            'milvus_collection_name': args.milvus_collection_name
        })

    # Upload to vector storage
    await upload_files_to_vector_storage(files, args.database, **db_params)


def main():
    """Main entry point for the CLI application."""
    parser = create_parser()
    args = parser.parse_args()

    # Run the async main function
    asyncio.run(async_main(args))


if __name__ == "__main__":
    main()
