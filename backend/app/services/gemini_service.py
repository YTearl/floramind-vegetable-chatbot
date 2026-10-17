"""
Google Gemini LLM Service
Uses the official google-genai SDK to generate grounded vegetable cultivation responses.
Includes a graceful offline knowledge synthesis fallback when GEMINI_API_KEY is not set.
"""

from typing import List, Dict, Any, Generator, Optional
from app.config import settings
from app.prompt_templates import FLORAMIND_SYSTEM_PROMPT, build_floramind_prompt
from app.services.rag_engine import rag_engine, check_out_of_scope_intent
from app.data.vegetable_database import search_vegetables

class GeminiService:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        self.model_name = settings.GEMINI_MODEL or "gemini-2.5-flash"
        self.client = None
        self._init_client()

    def _init_client(self):
        if self.api_key:
            try:
                from google import genai
                self.client = genai.Client(api_key=self.api_key)
                print(f"[Gemini Service] Initialized Google GenAI Client with model: {self.model_name}")
            except Exception as e:
                print(f"[Gemini Service] Client init notice: {e}")
                self.client = None
        else:
            self.client = None

    def update_credentials(self, api_key: str, model_name: Optional[str] = None):
        self.api_key = api_key
        if model_name:
            self.model_name = model_name
        self._init_client()

    def is_configured(self) -> bool:
        return bool(self.client and self.api_key)

    def generate_response(self, user_query: str, chat_history: List[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Generates a complete response for the user's query using RAG + Gemini.
        """
        # Step 1: Pre-screen for obvious out-of-scope queries
        if check_out_of_scope_intent(user_query):
            out_of_scope_reply = (
                "Hello! I am **Floramind**, an intelligent digital agricultural assistant specializing exclusively in "
                "**vegetable cultivation, scientific characteristics, planting schedules, and fertilizer management**.\n\n"
                "I am unable to answer questions outside of vegetable gardening and farming. "
                "Please feel free to ask me anything about growing vegetables, such as planting pechay, "
                "fertilizing tomatoes, ampalaya trellising, or harvesting timelines!"
            )
            return {
                "content": out_of_scope_reply,
                "sources": [],
                "model_used": "Floramind Guardrail",
                "is_out_of_scope": True
            }

        # Step 2: Retrieve relevant vegetable context via RAG (Hugging Face + Pinecone)
        context_str, retrieved_docs = rag_engine.retrieve_context(user_query, top_k=2)
        
        # Step 3: Call Gemini if client is ready
        if self.is_configured():
            try:
                from google.genai import types
                augmented_prompt = build_floramind_prompt(user_query, context_str, chat_history)
                
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=augmented_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=FLORAMIND_SYSTEM_PROMPT,
                        temperature=0.25,
                    )
                )
                
                sources = [doc.get("metadata", {}).get("name", "Agricultural Guide") for doc in retrieved_docs]
                return {
                    "content": response.text,
                    "sources": sources,
                    "model_used": self.model_name,
                    "is_out_of_scope": False
                }
            except Exception as e:
                print(f"[Gemini Service] Gemini API call error: {e}. Falling back to knowledge base synthesizer.")

        # Step 4: Fallback synthesizer using verified RAG documents
        fallback_content = self._synthesize_rag_response(user_query, context_str, retrieved_docs)
        sources = [doc.get("metadata", {}).get("name", "Agricultural Guide") for doc in retrieved_docs]
        
        return {
            "content": fallback_content,
            "sources": sources,
            "model_used": "Floramind RAG Engine (Local)",
            "is_out_of_scope": False
        }

    def generate_stream(self, user_query: str, chat_history: List[Dict[str, str]] = None) -> Generator[str, None, None]:
        """
        Streams response tokens.
        """
        if check_out_of_scope_intent(user_query):
            yield (
                "Hello! I am **Floramind**, an intelligent digital agricultural assistant specializing exclusively in "
                "**vegetable cultivation, scientific characteristics, planting schedules, and fertilizer management**.\n\n"
                "I am unable to answer questions outside of vegetable gardening and farming. "
                "Please feel free to ask me anything about growing vegetables, such as planting pechay, "
                "fertilizing tomatoes, ampalaya trellising, or harvesting timelines!"
            )
            return

        context_str, retrieved_docs = rag_engine.retrieve_context(user_query, top_k=2)

        if self.is_configured():
            try:
                from google.genai import types
                augmented_prompt = build_floramind_prompt(user_query, context_str, chat_history)
                
                response = self.client.models.generate_content_stream(
                    model=self.model_name,
                    contents=augmented_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=FLORAMIND_SYSTEM_PROMPT,
                        temperature=0.25,
                    )
                )
                for chunk in response:
                    if chunk.text:
                        yield chunk.text
                return
            except Exception as e:
                print(f"[Gemini Service] Streaming error: {e}")

        # Stream fallback in chunks for realistic typing effect
        complete_text = self._synthesize_rag_response(user_query, context_str, retrieved_docs)
        words = complete_text.split(" ")
        for i in range(0, len(words), 4):
            yield " ".join(words[i:i+4]) + " "

    def _synthesize_rag_response(self, query: str, context_str: str, retrieved_docs: List[Dict[str, Any]]) -> str:
        """
        Synthesizes formatted Floramind response from RAG documents if Gemini key is pending.
        Follows the strict required response format.
        """
        direct_matches = search_vegetables(query)
        if direct_matches:
            veg = direct_matches[0]
            cond = veg.get("ideal_conditions", {})
            fert = veg.get("fertilizer_recommendation", {})
            
            output = f"""Vegetable Name: {veg['name']}

Scientific Name: *{veg['scientific_name']}*

Vegetable Family: {veg['family']}

Planting Information:
- Planting Method: {veg['planting_method']}
- Germination Period: {veg['germination_period']}
- Recommended Seedling Age / Transplanting: {veg['seedling_age_transplant']}
- Ideal Growing Conditions: Temperature: {cond.get('temperature', 'Warm')}; Soil: {cond.get('soil_type', 'Well-drained loam')}, pH {cond.get('soil_ph', '6.0–6.8')}; Sunlight: {cond.get('sunlight', 'Full sun')}; Spacing: {cond.get('spacing', 'Standard')}

Days to Harvest: {veg['days_to_harvest']}

Days to Maturity: {veg['days_to_maturity']}

Harvesting Guide: {veg['harvesting_guide']}

Fertilizer Recommendation:
- Suitable Fertilizer Type: {fert.get('type', 'Organic compost & Complete 14-14-14')}
- Recommended Nutrients: {fert.get('nutrients', 'Balanced N-P-K')}
- Application Timing & Method: {fert.get('timing_method', 'Basal at planting, side-dress during growth')}
- Application Rate: {fert.get('rates_summary', 'Standard rate')} (Please specify your planting area in square meters for a precise dosage calculation).

Additional Growing Tips: {veg.get('growing_tips', 'Provide adequate moisture and check pests regularly.')}

---
*Note: Generated via Floramind Verified Agricultural Knowledge Base (DA-BPI / PCAARRD guidelines). For real-time multi-turn generative conversation, you can add your Google Gemini API Key in the Settings menu.*"""
            return output
            
        elif context_str:
            return f"""Vegetable Cultivation Guidance:

{context_str}

---
*Note: To enable dynamic conversational AI responses, please configure your Gemini API Key in Settings.*"""
        else:
            return (
                "I am Floramind, your vegetable cultivation assistant. I could not find a specific vegetable matching "
                "your query in the primary index. Could you please specify the name of the vegetable you are growing "
                "(e.g., Pechay, Tomato, Ampalaya, Sitaw, Eggplant, Okra, Lettuce)?\n\n"
                "If you would like a fertilizer calculation, please also let me know your planting area in square meters!"
            )

gemini_service = GeminiService()
