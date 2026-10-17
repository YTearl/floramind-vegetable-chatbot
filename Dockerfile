# ========================================================
# Floramind AI - Multi-Stage Dockerfile for Railway
# Builds React.js frontend & runs Python FastAPI backend
# ========================================================

# Stage 1: Build the React Frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend

COPY frontend/package*.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build

# Stage 2: Python 3.11 Backend
FROM python:3.11-slim
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/backend

# Install minimal build tools for python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python requirements
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy backend source code
COPY backend/ ./backend/

# Copy compiled React frontend from Stage 1
COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

# Expose default port
EXPOSE 8000

# Run FastAPI server on Railway dynamic $PORT
CMD ["sh", "-c", "python -m uvicorn app.main:app --app-dir backend --host 0.0.0.0 --port ${PORT:-8000}"]
