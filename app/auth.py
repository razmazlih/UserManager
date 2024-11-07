from app.models.token_model import TokenModel
import os

# טוקן ניהול מוגדר בקובץ .env
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

def authenticate_admin(token):
    return token == ADMIN_TOKEN

def load_app_tokens():
    return TokenModel.get_tokens()

# אין צורך במשתנה גלובלי; נטען את הטוקנים ישירות בתוך הפונקציה
def authenticate_token(token):
    valid_app_tokens = load_app_tokens()  # טוען את הטוקנים בכל פעם שמתבצע אימות
    for app_id, app_token in valid_app_tokens.items():
        if token == app_token:
            return app_id
    return None