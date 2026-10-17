import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from backend root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    # Google Gemini
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    # Pinecone Vector DB
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY", "")
    PINECONE_INDEX_NAME: str = os.getenv("PINECONE_INDEX_NAME", "floramind-vegetables")
    PINECONE_ENVIRONMENT: str = os.getenv("PINECONE_ENVIRONMENT", "us-east-1")

    # Hugging Face
    HUGGINGFACE_API_KEY: str = os.getenv("HUGGINGFACE_API_KEY", "")
    HF_EMBEDDING_MODEL: str = os.getenv("HF_EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

    # App Settings
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")

settings = Settings()
