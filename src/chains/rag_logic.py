from langchain_groq import ChatGroq
from langchain_community.vectorstores import Qdrant
from langchain_classic.chains import RetrievalQA
import os

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')

class RAGOrchestrator:
    def __init__(self):
        self.llm = ChatGroq(model='llama-3.1-8b-instant')

    async def run(self, query: str, session_id: str):
        response = self.llm.invoke(query)
        return response.content