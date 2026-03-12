"""채팅 API 요청/응답 스키마."""
from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    """사용자 메시지."""

    content: str = Field(..., min_length=1, description="채팅 메시지 내용")
    role: str = Field(default="user", description="역할: user | assistant | system")


class ChatRequest(BaseModel):
    """채팅 요청."""

    message: str = Field(..., min_length=1, description="사용자 입력 메시지")
    conversation_id: str | None = Field(default=None, description="대화 세션 ID (선택)")


class ChatResponse(BaseModel):
    """채팅 응답."""

    reply: str = Field(..., description="봇 응답")
    conversation_id: str | None = Field(default=None, description="대화 세션 ID")
