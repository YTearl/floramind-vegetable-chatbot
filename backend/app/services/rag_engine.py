"""
RAG (Retrieval-Augmented Generation) Engine
Coordinates Hugging Face embeddings, Pinecone vector search, and context assembly.
"""

from typing import List, Dict, Any, Tuple
from app.services.huggingface_service import hf_service
from app.services.pinecone_service import pinecone_service
from app.data.vegetable_database import VEGETABLE_DATA, search_vegetables

# Common non-vegetable indicator keywords for guardrail assistance
OUT_OF_SCOPE_KEYWORDS = [
    "car", "engine", "motorcycle", "vehicle", "crypto", "bitcoin", "ethereum",
    "python code", "javascript", "react", "c++", "programming", "hack",
    "stock market", "forex", "election", "politics", "president", "nba",
    "football", "fifa", "basketball", "movie", "celebrity", "actor", "laptop",
    "smartphone", "iphone", "android os", "pork", "beef", "chicken recipe",
    "pig farming", "poultry", "aquarium fish"
]

def check_out_of_scope_intent(query: str) -> bool:
    q_lower = query.lower()
    for kw in OUT_OF_SCOPE_KEYWORDS:
        # Check whole word boundary
        if f" {kw} " in f" {q_lower} ":
            return True
    return False

def build_vegetable_document_chunk(veg: Dict[str, Any]) -> str:
    """Creates a comprehensive text chunk for indexing and retrieval."""
    cond = veg.get("ideal_conditions", {})
    fert = veg.get("fertilizer_recommendation", {})
    
    chunk = f"""Vegetable Name: {veg['name']}
Scientific Name: {veg['scientific_name']}
Vegetable Family: {veg['family']}
Local / Common Names: {', '.join(veg.get('local_names', []))}

Planting Information:
- Planting Method: {veg['planting_method']}
- Germination Period: {veg['germination_period']}
- Recommended Seedling Age / Transplanting: {veg['seedling_age_transplant']}
- Temperature: {cond.get('temperature', 'N/A')}
- Soil Type: {cond.get('soil_type', 'N/A')}
- Soil pH: {cond.get('soil_ph', 'N/A')}
- Sunlight: {cond.get('sunlight', 'N/A')}
- Water Requirements: {cond.get('water_needs', 'N/A')}
- Spacing: {cond.get('spacing', 'N/A')}

Days to Harvest: {veg['days_to_harvest']}
Days to Maturity: {veg['days_to_maturity']}
Harvesting Guide: {veg['harvesting_guide']}

Fertilizer Recommendation:
- Suitable Fertilizer Type: {fert.get('type', 'N/A')}
- Nutrients: {fert.get('nutrients', 'N/A')}
- Timing & Method: {fert.get('timing_method', 'N/A')}
- Rates & Dosage: {fert.get('rates_summary', 'N/A')}

Additional Growing Tips: {veg.get('growing_tips', 'N/A')}
Verified Agricultural Citations: {', '.join(veg.get('citations', []))}
"""
    return chunk.strip()

class RAGEngine:
    def __init__(self):
        self.indexed = False

    def index_vegetables_into_vector_store(self, force: bool = False):
        """Indexes all vegetables into Pinecone and in-memory store."""
        if self.indexed and not force:
            return
            
        print("[RAG Engine] Generating Hugging Face embeddings for vegetable knowledge base...")
        vectors_to_upsert = []
        
        for veg in VEGETABLE_DATA:
            doc_text = build_vegetable_document_chunk(veg)
            # Generate embedding via Hugging Face
            emb = hf_service.get_embedding(doc_text)
            
            vectors_to_upsert.append({
                "id": f"veg_{veg['id']}",
                "values": emb,
                "metadata": {
                    "id": veg["id"],
                    "name": veg["name"],
                    "scientific_name": veg["scientific_name"],
                    "family": veg["family"],
                    "days_to_harvest": veg["days_to_harvest"],
                    "days_to_maturity": veg["days_to_maturity"],
                    "text": doc_text
                }
            })
            
        pinecone_service.upsert_vectors(vectors_to_upsert)
        self.indexed = True
        print(f"[RAG Engine] Successfully indexed {len(vectors_to_upsert)} vegetables into Vector Store.")

    def retrieve_context(self, query: str, top_k: int = 2) -> Tuple[str, List[Dict[str, Any]]]:
        """
        Embeds the query and retrieves the top_k matching agricultural documents.
        """
        if not self.indexed:
            self.index_vegetables_into_vector_store()
            
        # First check direct name match for instant precision
        direct_matches = search_vegetables(query)
        retrieved_docs = []
        
        if direct_matches:
            for dm in direct_matches[:top_k]:
                retrieved_docs.append({
                    "id": f"veg_{dm['id']}",
                    "score": 0.99,
                    "metadata": {
                        "name": dm["name"],
                        "scientific_name": dm["scientific_name"],
                        "text": build_vegetable_document_chunk(dm)
                    }
                })
        else:
            # Query vector store using Hugging Face embedding
            query_vector = hf_service.get_embedding(query)
            matches = pinecone_service.query(query_vector, top_k=top_k)
            retrieved_docs = matches

        # Combine text into context string
        context_parts = []
        for doc in retrieved_docs:
            meta = doc.get("metadata", {})
            text = meta.get("text", "")
            if text:
                context_parts.append(text)
                
        context_str = "\n\n---\n\n".join(context_parts)
        return context_str, retrieved_docs

rag_engine = RAGEngine()
