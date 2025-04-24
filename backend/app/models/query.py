from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    """Request model for user queries"""
    query: str = Field(..., min_length=1, description="User's question or query")

class QueryResponse(BaseModel):
    """Response model for Claude AI answers"""
    query: str = Field(..., description="Original user query")
    response: str = Field(..., description="Response from Claude AI")