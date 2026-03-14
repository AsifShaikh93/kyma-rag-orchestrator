from langchain_redis import RedisSemanticCache
from langchain_openai import OpenAIEmbeddings
from langchain_core.globals import set_llm_cache
import os

def init_semantic_cache():
    """
    Initializes a semantic cache using Redis Cloud. 
    This intercepts semantically similar questions to save LLM tokens.
    """

    host = os.getenv("REDIS_HOST")
    port = os.getenv("REDIS_PORT")
    password = os.getenv("REDIS_PASSWORD")
    
    redis_url = f"redis://:{password}@{host}:{port}"

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    semantic_cache = RedisSemanticCache(
        redis_url=redis_url,
        embeddings=embeddings,
        distance_threshold=0.1,
        ttl=3600  
    )

    set_llm_cache(semantic_cache)