import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FIREBASE_CREDENTIALS_PATH = os.getenv('FIREBASE_CREDENTIALS_PATH')
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')
    CORS_SUPPORTS_CREDENTIALS = bool(os.getenv('CORS_SUPPORTS_CREDENTIALS', True))

    DEBUG = os.getenv('DEBUG') == 'True'
    PORT = int(os.getenv('PORT')) or 5000

    ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
