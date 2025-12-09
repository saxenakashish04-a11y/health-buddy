# 🚀 Quick Deploy to PythonAnywhere - Follow These Steps

## ⚠️ IMPORTANT: I need your help for account creation

I can automate most steps, but you need to:
1. **Create your PythonAnywhere account** (username, email, password)
2. **Log in** to PythonAnywhere

After that, I can help automate the rest!

---

## Step-by-Step Process:

### STEP 1: Create Account (You do this - 2 minutes)
1. Go to: https://www.pythonanywhere.com/registration/register/beginner/
2. Fill in:
   - **Username:** (choose something unique, e.g., `healthbuddy2024`)
   - **Email:** (your email)
   - **Password:** (choose a password)
   - **Password (again):** (same password)
   - ✅ Check the terms checkbox
   - Complete the reCAPTCHA
3. Click **"Register"**
4. Check your email and verify your account

### STEP 2: Log In (You do this)
1. Go to: https://www.pythonanywhere.com/accounts/login/
2. Log in with your username and password

### STEP 3: After Login - Tell me!
Once you're logged in, tell me:
- Your PythonAnywhere username
- And I'll help automate the rest!

---

## What I'll automate for you:
✅ Clone your GitHub repository  
✅ Install dependencies  
✅ Configure the web app  
✅ Set up WSGI file  
✅ Deploy your API  

---

## Or... Do it manually (if you prefer):

After logging in, follow these commands in the **Bash console**:

```bash
# 1. Clone repository
cd ~
git clone https://github.com/saxenakashish04-a11y/health-buddy.git
cd health-buddy

# 2. Install dependencies
pip3.10 install --user fastapi uvicorn[standard] pydantic

# 3. Go to Web tab and create web app
# - Click "Web" tab
# - Click "Add a new web app"
# - Choose your domain
# - Select "Manual configuration"
# - Select Python 3.10
# - Set source code: /home/YOURUSERNAME/health-buddy
# - Edit WSGI file and paste the code from pythonanywhere_wsgi.py
# - Click "Reload"

# 4. Your app will be live at: https://YOURUSERNAME.pythonanywhere.com
```

---

**Ready? Create your account and let me know when you're logged in!** 🎉

