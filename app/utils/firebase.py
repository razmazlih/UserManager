import firebase_admin
from firebase_admin import credentials, firestore
from app.config import Config

def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(Config.FIREBASE_CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred)