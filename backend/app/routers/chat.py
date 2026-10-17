"""
Chat Router
Handles conversational queries, streaming SSE responses, and RAG context grounding.
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import json

from app.services.gemini_service import gemini_service

router = APIRouter(prefix="/api/chat", tags=["Chat"])

class ChatMessage(BaseModel):
    role: str # "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User's vegetable cultivation query")
    history: Optional[List[ChatMessage]] = Field(default=[], description="Previous conversation turns")
    stream: Optional[bool] = Field(default=False, description="Enable Server-Sent Events streaming")

class ChatResponse(BaseModel):
    reply: str
    sources: List[str]
    model: str
    is_out_of_scope: bool

@router.post("", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    history_dicts = [{"role": m.role, "content": m.content} for m in request.history]

    if request.stream:
        def event_generator():
            for chunk in gemini_service.generate_stream(request.message, history_dicts):
                yield f"data: {json.dumps({'chunk': chunk})}\n\n"
            yield "data: [DONE]\n\n"

        return StreamingResponse(event_generator(), media_type="text/event-stream")
    else:
        result = gemini_service.generate_response(request.message, history_dicts)
        return ChatResponse(
            reply=result["content"],
            sources=result["sources"],
            model=result["model_used"],
            is_out_of_scope=result["is_out_of_scope"]
        )
