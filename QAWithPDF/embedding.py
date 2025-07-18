from llama_index.core import VectorStoreIndex
from llama_index.core import ServiceContext
from llama_index.core import Settings
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import customexception
from logger import logging

def download_gemini_embedding(model, document):
    import shutil, os
    try:
        if os.path.exists("storage"):
            shutil.rmtree("storage")

        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20

        index = VectorStoreIndex.from_documents(document)
        index.storage_context.persist()

        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e, sys)
