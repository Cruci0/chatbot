"""채팅봇 비즈니스 로직 (AI 연동은 여기서 확장)."""
import uuid

# 나중에 OpenAI, Claude 등 LLM 연동 시 여기서 호출
# from openai import OpenAI


def get_chat_reply(message: str, conversation_id: str | None = None) -> tuple[str, str]:
    """
    사용자 메시지에 대한 봇 응답 생성.

    현재는 에코 응답. 실제 AI는 openai / anthropic 등 연동 후 구현.
    """
    cid = conversation_id or str(uuid.uuid4())
    # TODO: LLM API 호출로 교체
    reply = f"[에코] {message}"
    return reply, cid
