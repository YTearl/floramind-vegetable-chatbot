@echo off
title Floramind Vegetable Cultivation AI
echo ========================================================
echo   Floramind AI - Vegetable Gardening & Cultivation
echo   Backend: Python (FastAPI + Gemini + Pinecone + HF)
echo   Frontend: React.js (Vite + Modern Botanical Design)
echo ========================================================
echo.

echo Starting Python FastAPI Backend on port 8000...
start "Floramind Backend" cmd /k "cd /d %~dp0backend && python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload"

echo Starting React Frontend on port 5173...
start "Floramind Frontend" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo Both servers have been launched!
echo Open your browser at: http://localhost:5173
echo API Documentation: http://127.0.0.1:8000/docs
echo ========================================================
pause
