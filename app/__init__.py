from flask import Flask
from flask_cors import CORS
from .config import Config
from .utils.firebase import initialize_firebase
from .routes import user_routes, app_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # אתחול Firebase Firestore
    initialize_firebase()

    # הגדרת CORS על בסיס config
    cors_origins = Config.CORS_ORIGINS.split(',') if Config.CORS_ORIGINS != '*' else '*'
    CORS(app, resources={r"/*": {"origins": cors_origins}}, supports_credentials=Config.CORS_SUPPORTS_CREDENTIALS)

    # רישום הנתיבים
    app.register_blueprint(user_routes)
    app.register_blueprint(app_routes)

    return app