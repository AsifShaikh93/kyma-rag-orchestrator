from qdrant_client import QdrantClient
from langchain_community.vectorstores import Qdrant
from langchain_openai import OpenAIEmbeddings
import os

os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')

class QdrantProvider:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            client = QdrantClient(
                url=os.getenv("QDRANT_URL"),
                api_key=os.getenv("QDRANT_API_KEY"),
            )
            embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
            
            cls._instance = Qdrant(
                client=client, 
                collection_name="kyma-docs", 
                embeddings=embeddings
            )
        return cls._instance