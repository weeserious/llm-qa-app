import logging
import sys
from pydantic import BaseModel
from typing import Dict, Any, Optional

class LogConfig(BaseModel):
    """Logging configuration"""
    LOGGER_NAME: str = "claude_qa_api"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "INFO"

    version: int = 1
    disable_existing_loggers: bool = False
    formatters: Dict[str, Dict[str, str]] = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers: Dict[str, Dict[str, Any]] = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers: Dict[str, Dict[str, Any]] = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL, "propagate": False},
    }

def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get the logger for the specified name.
    
    Args:
        name: The name for the logger, defaults to the main logger
    
    Returns:
        The configured logger
    """
    logger_name = LogConfig().LOGGER_NAME
    if name:
        logger_name = f"{logger_name}.{name}"
    
    return logging.getLogger(logger_name)

def setup_logging():
    """Configure basic logging for the application"""
    logging_config = LogConfig()
    
    logging.basicConfig(
        level=logging_config.LOG_LEVEL,
        format=logging_config.LOG_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)]
    )