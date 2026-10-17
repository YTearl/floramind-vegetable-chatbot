"""
Floramind Backend Application Entrypoint
FastAPI server powering Floramind Vegetable Gardening & Cultivation AI.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from pathlib import Path

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

# Register API Routers first
app.include_router(chat.router)
app.include_router(vegetables.router)
app.include_router(calculator.router)
app.include_router(admin.router)

# Locate frontend dist if built
possible_dist_paths = [
    Path(__file__).resolve().parent.parent.parent / "frontend" / "dist",
    Path("/app/frontend/dist"),
    Path(__file__).resolve().parent.parent / "dist",
    Path("frontend/dist")
]

frontend_dist = None
for p in possible_dist_paths:
    if p.exists() and (p / "index.html").exists():
        frontend_dist = p
        break

if frontend_dist:
    print(f"[Floramind] Serving compiled React frontend from: {frontend_dist}")
    assets_dir = frontend_dist / "assets"
    if assets_dir.exists():
        app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")

    @app.get("/")
    async def serve_index():
        return FileResponse(frontend_dist / "index.html")

    @app.get("/{full_path:path}")
    async def serve_spa_route(full_path: str):
        if full_path.startswith("api/") or full_path.startswith("docs") or full_path.startswith("openapi.json"):
            return None
        target_file = frontend_dist / full_path
        if target_file.is_file():
            return FileResponse(target_file)
        return FileResponse(frontend_dist / "index.html")
else:
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
