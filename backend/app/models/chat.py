from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

class ChatMessage(BaseModel):
    """Model for a single chat message"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    query: str
    response: str
    timestamp: datetime = Field(default_factory=datetime.now)

class ChatHistory(BaseModel):
    """Model for chat history"""
    messages: List[ChatMessage] = []