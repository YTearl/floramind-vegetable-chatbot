"""
Admin & Health Router
Provides service status, live credentials configuration, and vector index triggers.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from app.config import settings
from app.services.gemini_service import gemini_service
from app.services.pinecone_service import pinecone_service
from app.services.huggingface_service import hf_service
from app.services.rag_engine import rag_engine

router = APIRouter(prefix="/api/admin", tags=["Admin & Health"])

class CredentialsUpdateRequest(BaseModel):
    gemini_api_key: Optional[str] = None
    gemini_model: Optional[str] = None
    pinecone_api_key: Optional[str] = None
    pinecone_index: Optional[str] = None
    huggingface_api_key: Optional[str] = None

@router.get("/status")
async def get_system_status():
    return {
        "status": "online",
        "gemini": {
            "configured": gemini_service.is_configured(),
            "model": gemini_service.model_name,
            "has_key": bool(settings.GEMINI_API_KEY)
        },
        "pinecone": {
            "connected": pinecone_service.is_connected,
            "index_name": pinecone_service.index_name,
            "vector_count": pinecone_service.count(),
            "mode": "Pinecone Cloud" if pinecone_service.is_connected else "In-Memory Vector Store (Ready)"
        },
        "huggingface": {
            "embedding_model": hf_service.model_name,
            "dimension": hf_service.dimension,
            "has_key": bool(settings.HUGGINGFACE_API_KEY),
            "engine": "SentenceTransformers (all-MiniLM-L6-v2) / Hugging Face Hub"
        }
    }

@router.post("/settings")
async def update_settings(req: CredentialsUpdateRequest):
    updated = []
    if req.gemini_api_key is not None:
        settings.GEMINI_API_KEY = req.gemini_api_key.strip()
        gemini_service.update_credentials(settings.GEMINI_API_KEY, req.gemini_model or settings.GEMINI_MODEL)
        updated.append("gemini")
        
    if req.gemini_model is not None and req.gemini_model.strip():
        settings.GEMINI_MODEL = req.gemini_model.strip()
        gemini_service.update_credentials(settings.GEMINI_API_KEY, settings.GEMINI_MODEL)
        updated.append("gemini_model")

    if req.pinecone_api_key is not None:
        settings.PINECONE_API_KEY = req.pinecone_api_key.strip()
        pinecone_service.api_key = settings.PINECONE_API_KEY
        if req.pinecone_index:
            settings.PINECONE_INDEX_NAME = req.pinecone_index.strip()
            pinecone_service.index_name = settings.PINECONE_INDEX_NAME
        pinecone_service.initialize_pinecone()
        updated.append("pinecone")

    if req.huggingface_api_key is not None:
        settings.HUGGINGFACE_API_KEY = req.huggingface_api_key.strip()
        hf_service.api_key = settings.HUGGINGFACE_API_KEY
        updated.append("huggingface")

    return {
        "success": True,
        "updated": updated,
        "message": f"Updated settings for: {', '.join(updated) if updated else 'none'}"
    }

@router.post("/index-pinecone")
async def trigger_pinecone_index():
    rag_engine.index_vegetables_into_vector_store(force=True)
    return {
        "success": True,
        "indexed_count": pinecone_service.count(),
        "mode": "Pinecone Cloud" if pinecone_service.is_connected else "In-Memory Vector Store"
    }
