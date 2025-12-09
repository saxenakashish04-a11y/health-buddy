# This file is for PythonAnywhere deployment
# WSGI configuration for FastAPI

import sys
import os

# Add your project directory to the path
project_dir = os.path.expanduser('~/health-buddy')
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Change to the project directory
os.chdir(project_dir)

# Import the FastAPI app
from main import app
from asgiref.wsgi import WsgiToAsgi

# Convert ASGI app to WSGI for PythonAnywhere
application = WsgiToAsgi(app)

