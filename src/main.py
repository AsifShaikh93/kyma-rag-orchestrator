import time
from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, make_asgi_app
from src.chains.rag_logic import RAGOrchestrator
from src.utils.cache import init_semantic_cache
from pydantic import BaseModel

class QueryRequest(BaseModel):
    user_input: str
    session_id: str

app = FastAPI(title="Auto-Scaling RAG Orchestrator")

IN_PROGRESS = Counter("rag_active_requests_total", "Total requests currently being handled")
LATENCY = Histogram("rag_llm_latency_seconds", "Time spent waiting for LLM response")

orchestrator = RAGOrchestrator()

@app.on_event("startup")
def startup_event():
    init_semantic_cache()

@app.post("/query")
async def handle_query(request: QueryRequest):
    IN_PROGRESS.inc()
    start_time = time.time()
    
    try:
        response = await orchestrator.run(request.user_input, request.session_id)
        duration = time.time() - start_time
        LATENCY.observe(duration)
        return {"answer": response, "latency": f"{duration:.2f}s"}
        
    finally:
        IN_PROGRESS.dec()

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)