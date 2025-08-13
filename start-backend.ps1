Write-Host "Starting ChatBoat Backend..." -ForegroundColor Green
Write-Host ""
Write-Host "Make sure you have Python installed and dependencies are installed." -ForegroundColor Yellow
Write-Host "If you haven't installed dependencies yet, run: pip install -r chatbot-backend/requirements.txt" -ForegroundColor Yellow
Write-Host ""

Set-Location chatbot-backend
python main.py

