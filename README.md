# Chatbot AI (FastAPI)

FastAPI + Uvicorn 기반 채팅봇 API 프로젝트입니다.

## 프로젝트 구조

```
chatbot/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI 앱 진입점
│   ├── config.py        # 설정 (환경 변수)
│   ├── models/          # Pydantic 요청/응답 스키마
│   │   ├── __init__.py
│   │   └── chat.py
│   ├── routers/         # API 라우터
│   │   ├── __init__.py
│   │   └── chat.py
│   └── services/        # 비즈니스 로직 (AI 연동)
│       ├── __init__.py
│       └── chat_service.py
├── .env.example
├── requirements.txt
└── README.md
```

## 실행 방법

1. 가상환경 생성 및 활성화 (권장)

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   ```

2. 의존성 설치

   ```bash
   pip install -r requirements.txt
   ```

3. 서버 실행

   ```bash
   uvicorn app.main:app --reload
   ```

4. 브라우저에서 API 문서 확인

   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## API 예시

- `GET /` - API 정보
- `GET /health` - 헬스 체크
- `POST /api/chat/` - 채팅 메시지 전송 → 봇 응답 수신

현재 채팅은 에코 응답입니다. 실제 AI 연동은 `app/services/chat_service.py`에서 LLM API를 호출하도록 수정하면 됩니다.

---

## 동작 예시: models/chat.py가 하는 일

**1. 클라이언트가 보내는 것 (JSON)**  
→ `ChatRequest`로 “이 형식이어야 한다”고 정의해 둔 것과 맞는지 검사합니다.

```json
{
  "message": "날씨 어때?",
  "conversation_id": null
}
```

- `message` 없으면 → 422 에러 (필수라서)
- `message`가 빈 문자열 `""` 이면 → 422 에러 (`min_length=1`)

**2. 라우터에서 쓰는 방식** (`routers/chat.py`)

```python
def chat(request: ChatRequest):   # ← 여기서 JSON이 ChatRequest로 검증됨
    reply, cid = get_chat_reply(
        message=request.message,           # request.message → "날씨 어때?"
        conversation_id=request.conversation_id,
    )
    return ChatResponse(reply=reply, conversation_id=cid)  # ← 응답도 형식 고정
```

**3. 서버가 돌려주는 것 (JSON)**  
→ `ChatResponse` 형식으로만 나가게 됩니다.

```json
{
  "reply": "[에코] 날씨 어때?",
  "conversation_id": "a1b2c3d4-..."
}
```

**4. 한 줄 요약**  
`models/chat.py` = “들어오는 JSON은 이렇게, 나가는 JSON은 이렇게” 규칙을 정해 두고, FastAPI가 그걸로 **검증 + 문서(/docs)** 에 쓰는 파일입니다.
