"""채팅 API 라우터."""
from fastapi import APIRouter, HTTPException

from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import get_chat_reply

router = APIRouter()


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    채팅 메시지를 보내고 봇 응답을 받습니다.
    """
    try:
        reply, conversation_id = get_chat_reply(
            message=request.message,
            conversation_id=request.conversation_id,
        )
        return ChatResponse(reply=reply, conversation_id=conversation_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
