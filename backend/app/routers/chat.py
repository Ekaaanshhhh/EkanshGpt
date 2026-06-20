from fastapi import APIRouter, HTTPException

from app.models.schemas import ChatRequest, ChatResponse
from app.services.chat_service import generate_chat_response
from app.utils.logger import logger

router = APIRouter()

@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    EkanshGPT Chat Endpoint.
    Accepts a question, retrieves context from ChromaDB, and generates an answer using Llama 3.3.
    """
    try:
        # Business logic strictly encapsulated in the service
        answer, sources = generate_chat_response(request.question)
        
        return ChatResponse(
            answer=answer,
            sources=sources
        )
        
    except ValueError as e:
        # ValueErrors raised from the service denote known/expected failures
        logger.error(f"Chat error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        # Catch-all for unexpected crashes
        logger.exception("Unexpected error in chat endpoint")
        raise HTTPException(status_code=500, detail="Internal server error while processing chat.")
