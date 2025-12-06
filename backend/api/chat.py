from fastapi import APIRouter
from pydantic import BaseModel
from backend.service.chat_service import chat_reply

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    session_id: str

class ChatResponse(BaseModel):
    response: str
    status: str
    session_id: str

@router.post("/chat")
async def chat(request: ChatRequest):
    ai_response = chat_reply(request.message)
    return ChatResponse(
        response=ai_response,
        status="success",
        session_id=request.session_id
    )
