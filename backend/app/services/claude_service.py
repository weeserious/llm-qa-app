import httpx
from app.core.config import settings

async def get_claude_response(query: str) -> str:
    """
    Get a response from the Claude AI API.
    
    Args:
        query: The user query to process
        
    Returns:
        Response text from Claude AI
        
    Raises:
        Exception: If the API request fails
    """
    if not settings.ANTHROPIC_API_KEY:
        raise ValueError("Missing Claude API key. Please set ANTHROPIC_API_KEY in .env file.")
    
    headers = {
        "x-api-key": settings.ANTHROPIC_API_KEY,
        "content-type": "application/json",
        "anthropic-version": "2023-06-01"
    }
    
   
    system_prompt = """

    You are a specialized AI assistant focused exclusively on HP laptops.

    Your role is to provide:

    Detailed information about HP laptop models
    Technical specifications
    Buying advice
    Troubleshooting guidance
    Comparisons between different HP laptop series

    Key guidelines:

    1. Only discuss HP laptop-related topics

    2. Provide accurate and up-to-date information

    3. Use clear, structured responses

    4. If a query is not about HP laptops, politely explain that you can only discuss HP laptops


    When answering questions, include:

    Specific model details
    Performance characteristics
    Price ranges
    Recommended use cases
    Current product lineup

    If you don't have specific information about an HP laptop query, admit the limitation transparently.

    """
    
    model_name = "claude-3-5-haiku-20241022"
    
    data = {
        "model": model_name,
        "max_tokens": settings.MAX_TOKENS,
        "temperature": 0.7,
        "system": system_prompt,
        "messages": [
            {"role": "user", "content": query}
        ]
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=data
        )
        
        if response.status_code != 200:
            error_detail = "Unknown error"
            try:
                error_data = response.json()
                error_detail = str(error_data)
            except:
                error_detail = response.text
                
            raise Exception(f"Claude API request failed with status {response.status_code}: {error_detail}")
        
        response_data = response.json()
        return response_data["content"][0]["text"]