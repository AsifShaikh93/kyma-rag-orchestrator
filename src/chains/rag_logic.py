from langchain_groq import ChatGroq
from langchain_community.vectorstores import Qdrant
from langchain_classic.chains import RetrievalQA
import os
import asyncio

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')

class RAGOrchestrator:
    def __init__(self):
        self.llm = ChatGroq(model='llama-3.1-8b-instant')

    async def run(self, query: str, session_id: str):
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: self.llm.invoke(query)
        )
        return response.content