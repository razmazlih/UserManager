from app.models.token_model import TokenModel
from app.config import Config

def authenticate_admin(token):
    return token == Config.ADMIN_TOKEN

def load_app_tokens():
    return TokenModel.get_tokens()

def authenticate_token(token):
    valid_app_tokens = load_app_tokens()
    for app_id, app_token in valid_app_tokens.items():
        if token == f'Bearer {app_token}':
            return app_id
    return None