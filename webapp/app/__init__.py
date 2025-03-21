import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes