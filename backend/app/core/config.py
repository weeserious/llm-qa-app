import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """Application settings"""
    API_TITLE: str = "Claude AI Q&A API"
    API_DESCRIPTION: str = "A FastAPI application integrating with Claude AI for Q&A"
    API_VERSION: str = "0.1.0"
    
    CORS_ORIGINS: list = ["*"]
    
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-3-sonnet-20240229")
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "1000"))
    
    class Config:
        case_sensitive = True

settings = Settings()