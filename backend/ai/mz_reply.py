import os
from dotenv import load_dotenv
load_dotenv()

# openai >=1.0.0 client 방식 사용
from openai import OpenAI

client = OpenAI()

def llm_reply(message: str) -> str:
    """OpenAI GPT 모델에 메시지 보내고 답변 받기 (openai>=1.0.0 호환).

    환경변수 `OPENAI_API_KEY`가 설정되어 있어야 합니다.
    """
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("환경변수 OPENAI_API_KEY가 설정되어 있지 않습니다. .env 또는 세션 환경변수에 추가하세요.")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "너는 친절한 AI 챗봇이야."},
            {"role": "user", "content": message}
        ]
    )

    # 새 클라이언트의 응답 객체에서 메시지 내용 추출
    try:
        return response.choices[0].message.content
    except Exception:
        try:
            # 안전한 대체 접근
            return response.choices[0].message["content"]
        except Exception:
            return str(response)
