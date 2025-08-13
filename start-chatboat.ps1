Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    ChatBoat - Full Stack Chatbot" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "This script will start both backend and frontend services." -ForegroundColor White
Write-Host ""
Write-Host "Prerequisites:" -ForegroundColor Yellow
Write-Host "- Python 3.8+ installed and in PATH" -ForegroundColor Yellow
Write-Host "- Node.js 18+ installed" -ForegroundColor Yellow
Write-Host "- Angular CLI 16+ installed globally" -ForegroundColor Yellow
Write-Host ""
Write-Host "If you haven't installed dependencies yet:" -ForegroundColor Yellow
Write-Host "- Backend: pip install -r chatbot-backend/requirements.txt" -ForegroundColor Yellow
Write-Host "- Frontend: cd chatbot-frontend && npm install" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press any key to continue..." -ForegroundColor Green
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

Write-Host ""
Write-Host "Starting Backend (FastAPI)..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd chatbot-backend; python main.py" -WindowStyle Normal

Write-Host ""
Write-Host "Waiting 5 seconds for backend to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

Write-Host ""
Write-Host "Starting Frontend (Angular)..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd chatbot-frontend; ng serve --open" -WindowStyle Normal

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Services are starting..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Backend:  http://localhost:8000" -ForegroundColor White
Write-Host "Frontend: http://localhost:4200" -ForegroundColor White
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor White
Write-Host ""
Write-Host "Press any key to exit this launcher..." -ForegroundColor Green
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

