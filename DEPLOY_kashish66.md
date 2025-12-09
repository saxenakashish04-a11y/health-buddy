# 🚀 Deployment Guide for kashish66

## Your Health Buddy API will be live at:
**https://kashish66.pythonanywhere.com**

---

## Step-by-Step Instructions:

### STEP 1: Log In to PythonAnywhere
1. Go to: https://www.pythonanywhere.com/accounts/login/
2. Log in with username: `kashish66` and your password

### STEP 2: Open Bash Console
1. After logging in, click the **"Consoles"** tab at the top
2. Click **"Bash"** (or "Start a new console" → "Bash")

### STEP 3: Clone Your Repository
Copy and paste these commands one by one in the Bash console:

```bash
cd ~
git clone https://github.com/saxenakashish04-a11y/health-buddy.git
cd health-buddy
ls
```

You should see your files listed!

### STEP 4: Install Dependencies
Run this command:

```bash
pip3.10 install --user fastapi uvicorn[standard] pydantic
```

Wait for it to finish installing (may take 1-2 minutes).

### STEP 5: Create Web App
1. Click the **"Web"** tab at the top
2. Click **"Add a new web app"** button
3. Choose domain: **`kashish66.pythonanywhere.com`** (should be selected by default)
4. Click **"Next"**
5. Select **"Manual configuration"** (NOT Flask or Django)
6. Select **Python 3.10**
7. Click **"Next"**

### STEP 6: Configure Source Code
1. In the **"Code"** section, find **"Source code"**
2. Set it to: `/home/kashish66/health-buddy`
3. Leave **"Working directory"** empty or set to: `/home/kashish66/health-buddy`

### STEP 7: Configure WSGI File
1. Scroll down to **"WSGI configuration file"**
2. Click on the file path (it will open an editor)
3. **DELETE ALL THE DEFAULT CODE** in the editor
4. **PASTE THIS CODE** instead:

```python
import sys
import os

project_dir = os.path.expanduser('~/health-buddy')
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

os.chdir(project_dir)

from main import app
application = app
```

5. Click **"Save"** button

### STEP 8: Reload Your Web App
1. Scroll to the top of the Web tab
2. Click the big green **"Reload"** button
3. Wait 10-20 seconds

### STEP 9: Test Your API! 🎉
Open these URLs in your browser:

- **Home:** https://kashish66.pythonanywhere.com/
- **API Docs:** https://kashish66.pythonanywhere.com/docs
- **Health Check:** https://kashish66.pythonanywhere.com/health
- **Tips:** https://kashish66.pythonanywhere.com/tips

---

## ✅ That's it! Your Health Buddy API is now live!

### Available Endpoints:
- `GET /` - Home page
- `GET /health` - Health check
- `GET /tips` - Health tips
- `POST /bmi` - BMI calculator
- `POST /symptoms/assess` - Symptom assessment
- `GET /docs` - Interactive API documentation

---

## ⚠️ Troubleshooting:

**If you get an error:**
1. Go to **"Web"** tab → **"Error log"** to see what went wrong
2. Common issues:
   - **Module not found:** Run `pip3.10 install --user fastapi uvicorn[standard] pydantic` again
   - **Import error:** Check that WSGI file path is correct
   - **Port error:** Make sure you're using Manual configuration, not Flask

**If the site doesn't load:**
- Wait 30-60 seconds after clicking Reload
- Check the Error log in the Web tab
- Make sure all dependencies installed successfully

---

**Need help? Let me know which step you're on!** 🚀

