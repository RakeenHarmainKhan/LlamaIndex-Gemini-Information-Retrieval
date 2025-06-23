# data_ingestion.py

from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging

def load_data(directory_path):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - directory_path (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents.
    """
    try:
        logging.info("Data loading started...")
        loader = SimpleDirectoryReader(directory_path)  # <--- use dynamic path
        documents = loader.load_data()
        logging.info("Data loading completed.")
        return documents
    except Exception as e:
        logging.info("Exception in loading data.")
        raise customexception(e, sys)
