from fastapi import APIRouter
from app.api.endpoints import query, chat, health

router = APIRouter()

router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"]
)

router.include_router(
    query.router,
    prefix="/query",
    tags=["Query"]
)

router.include_router(
    chat.router,
    prefix="/chat",
    tags=["Chat History"]
)