"""FastAPI 앱 진입점."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import chat

app = FastAPI(
    title=settings.app_name,
    description="채팅봇 AI API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/chat", tags=["chat"])


@app.get("/")
def root():
    """헬스 체크 및 API 정보."""
    return {"message": "Chatbot AI API", "docs": "/docs"}


@app.get("/health")
def health():
    """헬스 체크."""
    return {"status": "ok"}

@app.get("/weather")
def weather():
    """날씨 정보."""
    return {"status": "ok"}    
