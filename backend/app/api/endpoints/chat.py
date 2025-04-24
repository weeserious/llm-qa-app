from fastapi import APIRouter, HTTPException, status, Query
from app.models.chat import ChatMessage
from app.services.chat_service import get_chat_history, clear_chat_history
from typing import List

router = APIRouter()

@router.get(
    "/",
    response_model=List[ChatMessage],
    status_code=status.HTTP_200_OK,
    summary="Get chat history",
    description="Retrieves the chat history for a session"
)
async def retrieve_chat_history(
    session_id: str = Query(..., description="Unique identifier for the chat session")
):
    """
    Retrieve chat history for a session.
    
    The session ID is used to identify the chat session.
    """
    history = get_chat_history(session_id)
    return history

@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Clear chat history",
    description="Clears the chat history for a session"
)
async def delete_chat_history(
    session_id: str = Query(..., description="Unique identifier for the chat session")
):
    """
    Clear chat history for a session.
    
    The session ID is used to identify the chat session.
    """
    success = clear_chat_history(session_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No chat history found for session {session_id}"
        )