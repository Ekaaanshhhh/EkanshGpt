import os
import time
from typing import Tuple, List

from groq import Groq
from groq import APIError

from app.config import settings
from app.services.vector_store import get_collection, generate_embeddings
from app.utils.logger import logger

# Initialize the Groq Client globally
llm_client = Groq(api_key=settings.GROQ_API_KEY)

# Load the system prompt once on startup
PROMPT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prompts", "assistant_prompt.md")
try:
    with open(PROMPT_PATH, "r") as f:
        SYSTEM_PROMPT = f.read()
except FileNotFoundError:
    logger.error(f"Could not find system prompt at {PROMPT_PATH}")
    SYSTEM_PROMPT = "You are Eko, the portfolio assistant for Ekansh. Answer questions based on the context."

def generate_chat_response(question: str) -> Tuple[str, List[str]]:
    """
    End-to-end RAG pipeline:
    1. Embeds question.
    2. Retrieves top 3 chunks.
    3. Sends to Llama 3.3 70B via Groq API (with retry logic).
    4. Returns (answer_text, unique_sources).
    """
    logger.info(f"Generating chat response for question: {question}")
    
    # 1. Embed question
    try:
        emb = generate_embeddings([question])[0]
    except Exception as e:
        logger.error(f"Failed to generate query embedding: {e}")
        raise ValueError("Failed to process question embeddings.")

    # 2. Retrieve chunks
    try:
        collection = get_collection()
        res = collection.query(
            query_embeddings=[emb],
            n_results=3,  # Top 3 is sufficient and saves context window
            include=["documents", "metadatas", "distances"]
        )
        
        docs = res["documents"][0] if res["documents"] else []
        metas = res["metadatas"][0] if res["metadatas"] else []
        
    except Exception as e:
        logger.error(f"Failed to query ChromaDB: {e}")
        raise ValueError("Failed to retrieve context from database.")

    # Build context string and extract sources
    context_pieces = []
    sources_set = set()
    
    for i, doc in enumerate(docs):
        doc_name = metas[i].get("document_name", "Unknown Document")
        sources_set.add(doc_name)
        context_pieces.append(f"[Source: {doc_name}]\n{doc}")
        
    context_str = "\n\n".join(context_pieces)
    unique_sources = list(sources_set)

    # 3. Call LLM with simple retry for rate limits
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user", 
            "content": f"Context:\n{context_str}\n\nAnswer the following question using ONLY the context provided above.\nQuestion: {question}"
        }
    ]
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            logger.debug(f"Calling Groq LLM API (Attempt {attempt + 1})...")
            response = llm_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages, 
                max_tokens=500, 
                temperature=0.1
            )
            answer = response.choices[0].message.content.strip()
            logger.info("Successfully generated LLM answer.")
            return answer, unique_sources
            
        except APIError as e:
            if getattr(e, 'status_code', None) == 429:
                wait_time = (attempt + 1) * 2  # 2s, 4s, 6s
                logger.warning(f"Rate limited by Groq API (429). Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                logger.error(f"Groq API error: {e}")
                raise ValueError("Failed to generate response from the AI model.")
        except Exception as e:
            logger.error(f"Unexpected error calling LLM: {e}")
            raise ValueError("An unexpected error occurred while contacting the AI model.")
            
    # If we exhaust retries
    raise ValueError("AI Service is currently overloaded (Too Many Requests). Please try again later.")
