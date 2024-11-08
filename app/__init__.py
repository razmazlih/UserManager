from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.utils.firebase import initialize_firebase
from app.routes import admin_routes, user_routes, app_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # אתחול Firebase Firestore
    initialize_firebase()

    cors_origins = Config.CORS_ORIGINS.split(',') if Config.CORS_ORIGINS != '*' else '*'
    CORS(app, resources={r"/*": {"origins": cors_origins}})

    app.register_blueprint(user_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(app_routes)

    return app