from fastapi import APIRouter, status
import platform
import time

router = APIRouter()

start_time = time.time()

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Check if the API is running correctly"
)
async def health_check():
    """
    Health check endpoint for monitoring and uptime verification.
    
    Returns information about the API's status and environment.
    """
    return {
        "status": "ok",
        "uptime": time.time() - start_time,
        "python_version": platform.python_version(),
        "environment": "development"
    }