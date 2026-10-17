# Floramind AI — Intelligent Vegetable Gardening & Cultivation Chatbot

Floramind is a dedicated, science-based agricultural digital assistant designed exclusively for **vegetable gardening and cultivation**. It guides farmers, urban gardeners, students, and commercial growers with dependable, scientifically validated recommendations from seed sowing to harvest and nutrient management.

---

## 🌟 Tech Stack

- **Frontend**: **React.js** (Vite, modern botanical emerald aesthetic, custom Vanilla CSS, glassmorphism, responsive UI)
- **Backend**: **Python** (FastAPI, async REST API, SSE streaming, Pydantic validation)
- **LLM**: **Google Gemini** (Gemini 2.5 / 2.0 / Flash / Gemini 3.6 via official `google-genai` SDK)
- **Vector Database**: **Pinecone** (Serverless vector index with automatic cosine similarity retrieval + resilient in-memory fallback)
- **Embeddings & NLP**: **Hugging Face** (`sentence-transformers/all-MiniLM-L6-v2` locally cached + Hugging Face Hub Inference support)

---

## 📋 Core Capabilities & Strict Scope

Floramind specializes **exclusively in vegetables**:
1. **Scientific Identification**: Common names, Philippine local names, accepted scientific names, and botanical families.
2. **Planting Schedules**: Direct seeding vs. transplanting, seed germination days, seedling age, and spacing.
3. **Harvesting & Maturity Days**: Clear distinction between *Days to First Harvest*, *Days to Maturity*, and *Overall Harvesting Window*.
4. **Fertilizer Guidance**: Organic compost, balanced complete fertilizers (14-14-14), Urea (46-0-0), Potash (0-0-60), and precise square-meter plot dosages.
5. **Philippines Localization**: Tailored for Philippine lowland and highland crops (Pechay, Ampalaya, Sitaw, Talong, Kalabasa, Kamatis, Okra, Sili, Kangkong, etc.) incorporating DA-BPI, PCARRD, and UPLB-IPB research.
6. **Scope Restriction Guardrail**: Unrelated inquiries (e.g., cars, sports, non-vegetables, programming) are politely deflected with a reminder of Floramind's exclusive vegetable focus.

---

## 🚀 Quick Start

### 1. Launch Everything with 1-Click
Double click `run_app.bat` or run:
```bash
# Terminal 1: Start Backend (Python)
cd backend
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

# Terminal 2: Start Frontend (React)
cd frontend
npm run dev
```

### 2. Access the Application
- **Floramind Web Application**: [http://localhost:5173](http://localhost:5173)
- **Interactive OpenAPI Documentation**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔑 Environment Variables & API Keys (`backend/.env`)

Configure your keys in `backend/.env` or directly through the **Settings** modal in the web app:

```env
# Google Gemini
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash

# Pinecone Vector DB (Optional: Falls back to in-memory vector store if empty)
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_INDEX_NAME=floramind-vegetables
PINECONE_ENVIRONMENT=us-east-1

# Hugging Face
HUGGINGFACE_API_KEY=your_hf_token_here
HF_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

---

## 📚 Standard Response Template
When asked about any vegetable, Floramind formats its response strictly as:
- **Vegetable Name**: Common name
- **Scientific Name**: Accepted scientific name in italics
- **Vegetable Family**: Botanical family
- **Planting Information**: Method, germination days, seedling age, ideal conditions
- **Days to Harvest**: Estimated days until first harvest (noting starting point)
- **Days to Maturity**: Estimated maturity period and affecting factors
- **Harvesting Guide**: Visual readiness indicators and picking frequency
- **Fertilizer Recommendation**: Suitable types, N-P-K nutrient schedules, dosages
- **Additional Growing Tips**: Pest management, aeration, and yield optimization
