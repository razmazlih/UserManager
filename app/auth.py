from app.models.token_model import TokenModel
import os

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

def authenticate_admin(token):
    return token == ADMIN_TOKEN

def load_app_tokens():
    return TokenModel.get_tokens()

def authenticate_token(token):
    valid_app_tokens = load_app_tokens()
    for app_id, app_token in valid_app_tokens.items():
        if token == app_token:
            return app_id
    return None