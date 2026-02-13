from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/health", tags=["health"])
def health_chec():
    return { "status":"ok"}
