from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/")
async def serve_chat():
    return FileResponse("frontend/templates/chat.html")
