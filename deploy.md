# Quick Deploy Guide - Health Buddy API

Your app is ready to deploy! Follow these simple steps:

## Option 1: Deploy to Render (Recommended - Free)

1. Go to: https://render.com
2. Click "Get Started for Free" → Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect repository: `saxenakashish04-a11y/health-buddy`
5. Settings (auto-detected):
   - Name: `health-buddy`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Click "Create Web Service"
7. Wait 2-3 minutes → Your app is live! 🎉

## Option 2: Deploy to Railway (Faster)

1. Go to: https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select: `saxenakashish04-a11y/health-buddy`
5. Railway auto-deploys → Done! 🚀

## Your Live API Endpoints:

- `https://your-app-name.onrender.com/` - Home
- `https://your-app-name.onrender.com/docs` - Interactive API docs
- `https://your-app-name.onrender.com/health` - Health check
- `https://your-app-name.onrender.com/tips` - Health tips
- `https://your-app-name.onrender.com/bmi` - BMI calculator (POST)
- `https://your-app-name.onrender.com/symptoms/assess` - Symptom checker (POST)

## Test Your API:

```bash
# Health check
curl https://your-app-name.onrender.com/health

# Get tips
curl https://your-app-name.onrender.com/tips

# Calculate BMI
curl -X POST https://your-app-name.onrender.com/bmi \
  -H "Content-Type: application/json" \
  -d '{"height_cm": 175, "weight_kg": 70}'
```

