"""
Pinecone Vector Database Service
Manages index creation, document vector upserting, and top-k semantic similarity search.
Includes an in-memory vector fallback when Pinecone credentials are not configured.
"""

import math
from typing import List, Dict, Any, Optional
from app.config import settings

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)

class PineconeService:
    def __init__(self):
        self.api_key = settings.PINECONE_API_KEY
        self.index_name = settings.PINECONE_INDEX_NAME
        self.dimension = 384
        self.pc = None
        self.index = None
        self.is_connected = False
        
        # In-memory vector store fallback
        self.in_memory_docs: List[Dict[str, Any]] = []
        
        self.initialize_pinecone()

    def initialize_pinecone(self) -> bool:
        """Attempts connection to Pinecone cloud."""
        if not self.api_key:
            print("[Pinecone Service] No PINECONE_API_KEY provided. Operating in high-performance in-memory mode.")
            self.is_connected = False
            return False

        try:
            from pinecone import Pinecone, ServerlessSpec
            self.pc = Pinecone(api_key=self.api_key)
            
            # Check existing indexes
            existing_indexes = [idx["name"] if isinstance(idx, dict) else idx.name for idx in self.pc.list_indexes()]
            
            if self.index_name not in existing_indexes:
                print(f"[Pinecone Service] Creating Serverless index '{self.index_name}' (dim={self.dimension})...")
                self.pc.create_index(
                    name=self.index_name,
                    dimension=self.dimension,
                    metric="cosine",
                    spec=ServerlessSpec(cloud="aws", region="us-east-1")
                )
                
            self.index = self.pc.Index(self.index_name)
            self.is_connected = True
            print(f"[Pinecone Service] Connected to index '{self.index_name}' successfully.")
            return True
        except Exception as e:
            print(f"[Pinecone Service] Connection notice: {e}. Falling back to in-memory vector storage.")
            self.is_connected = False
            return False

    def upsert_vectors(self, vectors: List[Dict[str, Any]]) -> bool:
        """
        Upsert a list of vector dicts:
        [{ 'id': 'doc_1', 'values': [...], 'metadata': { 'text': '...', 'vegetable': 'pechay' } }]
        """
        # Always maintain in-memory copy for instant zero-latency retrieval
        for v in vectors:
            # Replace existing or append
            self.in_memory_docs = [d for d in self.in_memory_docs if d["id"] != v["id"]]
            self.in_memory_docs.append(v)
            
        if self.is_connected and self.index:
            try:
                # Upsert to Pinecone in batches of 100
                batch_size = 100
                for i in range(0, len(vectors), batch_size):
                    batch = vectors[i:i + batch_size]
                    formatted = [
                        (item["id"], item["values"], item.get("metadata", {}))
                        for item in batch
                    ]
                    self.index.upsert(vectors=formatted)
                return True
            except Exception as e:
                print(f"[Pinecone Service] Upsert error: {e}")
                return False
        return True

    def query(self, query_vector: List[float], top_k: int = 4) -> List[Dict[str, Any]]:
        """
        Queries top_k most similar documents.
        """
        if self.is_connected and self.index:
            try:
                res = self.index.query(
                    vector=query_vector,
                    top_k=top_k,
                    include_metadata=True
                )
                results = []
                for match in res.get("matches", []):
                    results.append({
                        "id": match.get("id"),
                        "score": match.get("score"),
                        "metadata": match.get("metadata", {})
                    })
                return results
            except Exception as e:
                print(f"[Pinecone Service] Query cloud error: {e}. Falling back to local vector search.")

        # Local in-memory cosine similarity search
        scored_docs = []
        for doc in self.in_memory_docs:
            score = cosine_similarity(query_vector, doc["values"])
            scored_docs.append({
                "id": doc["id"],
                "score": score,
                "metadata": doc.get("metadata", {})
            })
            
        scored_docs.sort(key=lambda x: x["score"], reverse=True)
        return scored_docs[:top_k]

    def count(self) -> int:
        if self.is_connected and self.index:
            try:
                stats = self.index.describe_index_stats()
                return stats.get("total_vector_count", len(self.in_memory_docs))
            except Exception:
                pass
        return len(self.in_memory_docs)

pinecone_service = PineconeService()
