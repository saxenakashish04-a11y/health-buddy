# Health Buddy - Quick Deploy Script
Write-Host "🚀 Opening Render deployment page..." -ForegroundColor Green
Write-Host ""
Write-Host "Your repository is ready: https://github.com/saxenakashish04-a11y/health-buddy" -ForegroundColor Cyan
Write-Host ""
Write-Host "Steps:" -ForegroundColor Yellow
Write-Host "1. Sign up/Login with GitHub" -ForegroundColor White
Write-Host "2. Click 'New +' → 'Web Service'" -ForegroundColor White
Write-Host "3. Select repository: saxenakashish04-a11y/health-buddy" -ForegroundColor White
Write-Host "4. Click 'Create Web Service' (settings are auto-detected)" -ForegroundColor White
Write-Host "5. Wait 2-3 minutes → Your app is live! 🎉" -ForegroundColor White
Write-Host ""

# Open Render in browser
Start-Process "https://render.com"

# Also open Railway as alternative
Write-Host "Alternative: Railway (faster setup)" -ForegroundColor Yellow
Start-Process "https://railway.app"

Write-Host ""
Write-Host "✅ Your code is already on GitHub and ready to deploy!" -ForegroundColor Green

