from app.models.chat import ChatMessage
from typing import List, Dict
import threading

chat_history: Dict[str, List[ChatMessage]] = {}
chat_lock = threading.Lock()

def save_chat_message(session_id: str, query: str, response: str) -> ChatMessage:
    """
    Save a chat message to the chat history.
    
    Args:
        session_id: Unique identifier for the chat session
        query: User's query
        response: AI's response
        
    Returns:
        The created ChatMessage
    """
    chat_message = ChatMessage(query=query, response=response)
    
    with chat_lock:
        if session_id not in chat_history:
            chat_history[session_id] = []
        
        chat_history[session_id].append(chat_message)
    
    return chat_message

def get_chat_history(session_id: str) -> List[ChatMessage]:
    """
    Get chat history for a session.
    
    Args:
        session_id: Unique identifier for the chat session
        
    Returns:
        List of ChatMessages for the session
    """
    with chat_lock:
        return chat_history.get(session_id, [])

def clear_chat_history(session_id: str) -> bool:
    """
    Clear chat history for a session.
    
    Args:
        session_id: Unique identifier for the chat session
        
    Returns:
        True if cleared, False if session not found
    """
    with chat_lock:
        if session_id in chat_history:
            chat_history[session_id] = []
            return True
        return False