from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Qdrant
from langchain_classic.chains import RetrievalQA
import os

os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')

class RAGOrchestrator:
    def __init__(self):
        self.llm = ChatOpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1",
            model_name="llama3-70b-8192"
        )

    async def run(self, query: str, session_id: str):
        response = self.llm.invoke(query)
        return response.content