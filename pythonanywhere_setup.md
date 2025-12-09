# PythonAnywhere Deployment Guide

## Steps to Deploy Health Buddy on PythonAnywhere (Free - No Card Required)

### Step 1: Sign Up
1. Go to https://www.pythonanywhere.com
2. Click "Beginner: Sign up for free account"
3. Create account (free tier available)

### Step 2: Upload Your Code
1. Go to "Files" tab
2. Click "Upload a file"
3. Or use Git: Go to "Consoles" → "Bash" → Run:
   ```bash
   git clone https://github.com/saxenakashish04-a11y/health-buddy.git
   cd health-buddy
   ```

### Step 3: Install Dependencies
In Bash console:
```bash
pip3.10 install --user fastapi uvicorn pydantic
```

### Step 4: Create WSGI File
Create file: `/var/www/yourusername_pythonanywhere_com_wsgi.py`
```python
import sys
path = '/home/yourusername/health-buddy'
if path not in sys.path:
    sys.path.insert(0, path)

from main import app
application = app
```

### Step 5: Configure Web App
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10
5. Set source code: `/home/yourusername/health-buddy`
6. Set WSGI file: `/var/www/yourusername_pythonanywhere_com_wsgi.py`
7. Click "Reload"

Your app will be at: `https://yourusername.pythonanywhere.com`

