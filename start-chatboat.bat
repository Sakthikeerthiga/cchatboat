@echo off
echo ========================================
echo    ChatBoat - Full Stack Chatbot
echo ========================================
echo.
echo This script will start both backend and frontend services.
echo.
echo Prerequisites:
echo - Python 3.8+ installed and in PATH
echo - Node.js 18+ installed
echo - Angular CLI 16+ installed globally
echo.
echo If you haven't installed dependencies yet:
echo - Backend: pip install -r chatbot-backend/requirements.txt
echo - Frontend: cd chatbot-frontend && npm install
echo.
echo Press any key to continue...
pause >nul

echo.
echo Starting Backend (FastAPI)...
start "ChatBoat Backend" cmd /k "cd chatbot-backend && python main.py"

echo.
echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak >nul

echo.
echo Starting Frontend (Angular)...
start "ChatBoat Frontend" cmd /k "cd chatbot-frontend && ng serve --open"

echo.
echo ========================================
echo Services are starting...
echo ========================================
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:4200
echo API Docs: http://localhost:8000/docs
echo.
echo Press any key to exit this launcher...
pause >nul

