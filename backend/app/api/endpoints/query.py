from fastapi import APIRouter, HTTPException, status, Query
from app.models.query import QueryRequest, QueryResponse
from app.services.claude_service import get_claude_response
from app.services.chat_service import save_chat_message
from app.core.validators import validate_query

router = APIRouter()

@router.post(
    "/",
    response_model=QueryResponse,
    status_code=status.HTTP_200_OK,
    summary="Process a user query",
    description="Sends the user query to Claude AI and returns the response"
)
async def process_query(
    request: QueryRequest,
    session_id: str = Query(..., description="Unique identifier for the chat session")
):
    """
    Process a user query and return a response from Claude AI.
    
    The query is sent to the Claude AI API and the response is returned.
    The chat history is updated with the query and response.
    """
    try:
        response = await get_claude_response(request.query)
        
        save_chat_message(session_id, request.query, response)
        
        return QueryResponse(
            query=request.query,
            response=response
        )
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing query: {str(e)}"
        )