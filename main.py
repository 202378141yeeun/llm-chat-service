from fastapi import FastAPI
from backend.api.chat import router as chat_router
from backend.api.basic import router as basic_router

app = FastAPI()

app.include_router(basic_router)
app.include_router(chat_router, prefix="/api")

# 실행: `uvicorn main:app --reload`