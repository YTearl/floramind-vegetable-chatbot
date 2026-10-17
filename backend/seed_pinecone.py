"""
Standalone Pinecone Seeder Script
Populates your Pinecone index with the Floramind Vegetable Knowledge Base.
Usage: python seed_pinecone.py
"""

import os
import sys
from pathlib import Path

# Add backend directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent))

from app.config import settings
from app.services.rag_engine import rag_engine
from app.services.pinecone_service import pinecone_service

def main():
    print("=" * 60)
    print("Floramind Vegetable AI - Pinecone Index Seeder")
    print("=" * 60)
    print(f"Target Index: {settings.PINECONE_INDEX_NAME}")
    print(f"Has API Key: {'Yes' if settings.PINECONE_API_KEY else 'No (using local fallback)'}")
    print("\nStarting indexing process...")
    
    rag_engine.index_vegetables_into_vector_store(force=True)
    
    print("\nIndexing complete!")
    print(f"Total documents indexed: {pinecone_service.count()}")
    print("Pinecone status:", "Connected to Cloud" if pinecone_service.is_connected else "Stored in local memory")
    print("=" * 60)

if __name__ == "__main__":
    main()
