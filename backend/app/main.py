"""
Floramind Backend Application Entrypoint
FastAPI server powering Floramind Vegetable Gardening & Cultivation AI.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import settings
from app.routers import chat, vegetables, calculator, admin
from app.services.rag_engine import rag_engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: seed and index vegetable knowledge base
    print("[Floramind] Starting up Floramind Vegetable AI...")
    try:
        rag_engine.index_vegetables_into_vector_store()
    except Exception as e:
        print(f"[Floramind] Knowledge indexing notice: {e}")
    yield
    print("[Floramind] Shutting down.")

app = FastAPI(
    title="Floramind Vegetable Cultivation AI API",
    description="Intelligent and reliable vegetable gardening and cultivation chatbot API powered by Gemini, Pinecone, and Hugging Face.",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Middleware for React frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(chat.router)
app.include_router(vegetables.router)
app.include_router(calculator.router)
app.include_router(admin.router)

@app.get("/")
async def root():
    return {
        "app": "Floramind AI",
        "tagline": "Intelligent and Reliable Vegetable Gardening and Cultivation Chatbot",
        "version": "1.0.0",
        "docs_url": "/docs",
        "endpoints": {
            "chat": "/api/chat",
            "vegetables": "/api/vegetables",
            "fertilizer_calculator": "/api/calculator/fertilizer",
            "status": "/api/admin/status"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
