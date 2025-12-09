# PythonAnywhere Deployment - Step by Step Guide

## ✅ Your Health Buddy API on PythonAnywhere (FREE - No Card Required!)

### Step 1: Sign Up
1. Go to https://www.pythonanywhere.com
2. Click **"Beginner: Sign up for free account"**
3. Create your account (it's completely free!)

### Step 2: Access Your Account
1. After signing up, you'll be in the dashboard
2. You'll see tabs: **Files**, **Consoles**, **Web**, **Tasks**, etc.

### Step 3: Clone Your Repository
1. Click on **"Consoles"** tab
2. Click **"Bash"** to open a terminal
3. Run these commands:
   ```bash
   cd ~
   git clone https://github.com/saxenakashish04-a11y/health-buddy.git
   cd health-buddy
   ls
   ```
   (This downloads your code)

### Step 4: Install Dependencies
In the same Bash console, run:
```bash
pip3.10 install --user fastapi uvicorn[standard] pydantic
```

### Step 5: Create WSGI File
1. Go to **"Files"** tab
2. Navigate to: `/home/yourusername/health-buddy/`
3. You should see `pythonanywhere_wsgi.py` (already created!)
4. If not, create a new file called `pythonanywhere_wsgi.py` with this content:
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

### Step 6: Configure Web App
1. Go to **"Web"** tab
2. Click **"Add a new web app"**
3. Choose domain: `yourusername.pythonanywhere.com` (free option)
4. Select **"Manual configuration"** (not Flask/Django)
5. Select **Python 3.10**
6. Click **"Next"**

### Step 7: Set Source Code and WSGI
1. In the **"Code"** section:
   - **Source code:** `/home/yourusername/health-buddy`
2. Scroll down to **"WSGI configuration file"**
3. Click on the file path (it will open an editor)
4. **Delete all the default code** and paste this:
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
5. Click **"Save"**

### Step 8: Configure Static Files (Optional)
- Leave static files mapping empty for now (FastAPI handles this)

### Step 9: Add Startup Task for Uvicorn
1. Go to **"Tasks"** tab
2. Click **"Create a new task"**
3. Set:
   - **Command:** `cd ~/health-buddy && uvicorn main:app --host 0.0.0.0 --port 8080`
   - **Hour:** Any hour
   - **Minute:** Any minute
   - **Enabled:** ✅ Check this
4. Click **"Create"**

### Step 10: Reload Web App
1. Go back to **"Web"** tab
2. Click the big green **"Reload"** button
3. Wait a few seconds

### Step 11: Test Your API!
Your app will be live at:
- **Home:** `https://yourusername.pythonanywhere.com/`
- **Docs:** `https://yourusername.pythonanywhere.com/docs`
- **Health:** `https://yourusername.pythonanywhere.com/health`
- **Tips:** `https://yourusername.pythonanywhere.com/tips`

---

## ⚠️ Important Notes:

1. **Replace `yourusername`** with your actual PythonAnywhere username everywhere
2. **Free tier limitations:**
   - App sleeps after 90 seconds of inactivity
   - First request after sleep takes ~30 seconds to wake up
   - Limited to 1 web app
3. **If you get errors:**
   - Check the **"Web"** tab → **"Error log"** for details
   - Make sure all dependencies are installed
   - Verify the WSGI file path is correct

---

## 🎉 That's it! Your Health Buddy API is now live!

