import uuid
from typing import Dict, Any
import json
from datetime import datetime

def generate_session_id() -> str:
    """
    Generate a unique session ID.
    
    Returns:
        A unique session ID as a string
    """
    return str(uuid.uuid4())

def format_response(response: str) -> str:
    """
    Format the response from Claude for better readability.
    
    Args:
        response: The raw response from Claude
        
    Returns:
        Formatted response
    """
    # This is a simple example - you could enhance this with
    # additional formatting as needed
    response = response.strip()
    return response

def safe_dict_to_json(data: Dict[str, Any]) -> str:
    """
    Safely convert a dictionary to a JSON string.
    
    Args:
        data: The dictionary to convert
        
    Returns:
        JSON string representation of the dictionary
    """
    class DateTimeEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return super().default(obj)
    
    return json.dumps(data, cls=DateTimeEncoder)