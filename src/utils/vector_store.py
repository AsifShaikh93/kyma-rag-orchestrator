from qdrant_client import QdrantClient
from langchain_community.vectorstores import Qdrant
from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ['HF_TOKEN']=os.getenv('HF_TOKEN')

class QdrantProvider:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            client = QdrantClient(
                url=os.getenv("QDRANT_URL"),
                api_key=os.getenv("QDRANT_API_KEY"),
            )
            embeddings=HuggingFaceEmbeddings()
            
            cls._instance = Qdrant(
                client=client, 
                collection_name="kyma-docs", 
                embeddings=embeddings
            )
        return cls._instance