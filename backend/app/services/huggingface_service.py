"""
Hugging Face Embedding Service
Supports local sentence-transformers (all-MiniLM-L6-v2) or Hugging Face Inference API,
with a robust fallback to guarantee continuous operation.
"""

import math
import hashlib
from typing import List, Union
from app.config import settings

_local_model = None
_model_failed = False

def get_sentence_transformer():
    global _local_model, _model_failed
    if _local_model is not None:
        return _local_model
    if _model_failed:
        return None
    try:
        from sentence_transformers import SentenceTransformer
        model_name = settings.HF_EMBEDDING_MODEL or "sentence-transformers/all-MiniLM-L6-v2"
        # Extract model repo if full path
        _local_model = SentenceTransformer(model_name)
        print(f"[HuggingFace Service] Loaded local SentenceTransformer: {model_name}")
        return _local_model
    except Exception as e:
        print(f"[HuggingFace Service] Local sentence-transformers init notice: {e}")
        _model_failed = True
        return None

def fallback_embed_text(text: str, dim: int = 384) -> List[float]:
    """
    Deterministic semantic hash embedding fallback (dimension 384).
    Ensures zero crashes even in extreme environments without torch weights.
    """
    words = text.lower().split()
    vector = [0.0] * dim
    if not words:
        return vector
        
    for i, word in enumerate(words):
        h = int(hashlib.sha256(word.encode("utf-8")).hexdigest(), 16)
        idx = h % dim
        sign = 1.0 if ((h >> 8) & 1) == 0 else -1.0
        weight = 1.0 / (1.0 + math.log1p(i))
        vector[idx] += sign * weight
        
    # L2 normalize
    norm = math.sqrt(sum(x * x for x in vector))
    if norm > 0:
        vector = [x / norm for x in vector]
    return vector

class HuggingFaceService:
    def __init__(self):
        self.api_key = settings.HUGGINGFACE_API_KEY
        self.model_name = settings.HF_EMBEDDING_MODEL
        self.dimension = 384

    def get_embedding(self, text: str) -> List[float]:
        """
        Generates 384-dimensional vector embedding for a text string.
        """
        # Try local model first
        model = get_sentence_transformer()
        if model is not None:
            try:
                emb = model.encode(text, normalize_embeddings=True)
                return emb.tolist()
            except Exception as e:
                print(f"[HuggingFace Service] Local encode error: {e}")

        # Try Hugging Face Hub Inference if API key provided
        if self.api_key:
            try:
                from huggingface_hub import InferenceClient
                client = InferenceClient(token=self.api_key)
                feature = client.feature_extraction(text, model=self.model_name)
                # Feature might be numpy array or list
                if hasattr(feature, "tolist"):
                    return feature.tolist()
                elif isinstance(feature, list):
                    return feature
            except Exception as e:
                print(f"[HuggingFace Service] HF Hub Inference error: {e}")

        # Deterministic semantic vector fallback
        return fallback_embed_text(text, self.dimension)

    def get_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        model = get_sentence_transformer()
        if model is not None:
            try:
                embs = model.encode(texts, normalize_embeddings=True)
                return embs.tolist()
            except Exception as e:
                print(f"[HuggingFace Service] Batch encode error: {e}")

        return [self.get_embedding(t) for t in texts]

hf_service = HuggingFaceService()
