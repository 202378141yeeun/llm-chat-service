from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "llm-chat-service 백엔드가 준비되었습니다."}

# 실행: `uvicorn main:app --reload`