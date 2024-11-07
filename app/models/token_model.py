from datetime import datetime
from firebase_admin import firestore

# פונקציה שמחזירה את חיבור Firestore בעת הצורך
def get_db():
    return firestore.client()

class TokenModel:
    @staticmethod
    def add_token(app_id, token):
        db = get_db()
        db.collection("tokens").document(app_id).set({
            "token": token,
            "updated_at": datetime.utcnow()
        })

    @staticmethod
    def update_token(app_id, token):
        db = get_db()
        db.collection("tokens").document(app_id).update({
            "token": token,
            "updated_at": datetime.utcnow()
        })

    @staticmethod
    def get_tokens():
        db = get_db()
        tokens_ref = db.collection("tokens").stream()
        return {token.id: token.to_dict()['token'] for token in tokens_ref}

    @staticmethod
    def delete_token(app_id):
        db = get_db()
        db.collection("tokens").document(app_id).delete()