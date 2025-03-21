import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # Configuration directory
    CONFIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config')
    os.makedirs(CONFIG_DIR, exist_ok=True)
    
    # Default BlockClock configuration file path
    DEFAULT_CONFIG_FILE = os.path.join(CONFIG_DIR, 'blockclock.conf')