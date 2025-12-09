# This file is for PythonAnywhere deployment
# Place this file in your home directory or web app directory

import sys
import os

# Add your project directory to the path
# Replace 'yourusername' with your PythonAnywhere username
project_dir = os.path.expanduser('~/health-buddy')
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Change to the project directory
os.chdir(project_dir)

# Import the FastAPI app
from main import app

# PythonAnywhere expects 'application' variable
application = app

