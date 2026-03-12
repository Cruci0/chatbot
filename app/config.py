"""애플리케이션 설정 (환경 변수 등)."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """환경 변수 기반 설정."""

    app_name: str = "Chatbot AI"
    debug: bool = False
    # AI API 키 등은 필요 시 여기에 추가
    # openai_api_key: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
