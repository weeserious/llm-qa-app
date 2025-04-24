from fastapi import HTTPException, status
import re

def validate_query(query: str):
    """
    Validate a user query.
    
    Args:
        query: The user query to validate
        
    Raises:
        HTTPException: If the query is invalid
    """
    if not query or not query.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Query cannot be empty"
        )
    
    if len(query) > 500:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Query cannot exceed 500 characters"
        )
    
    # Check for potentially harmful content (very basic check)
    harmful_patterns = [
        r'(?i)DROP\s+TABLE',
        r'(?i)DELETE\s+FROM',
        r'(?i)INSERT\s+INTO',
        r'(?i)SELECT\s+.*\s+FROM',
        r'(?i)UPDATE\s+.*\s+SET',
        r'(?i)<script>'
    ]
    
    for pattern in harmful_patterns:
        if re.search(pattern, query):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Query contains potentially harmful content"
            )