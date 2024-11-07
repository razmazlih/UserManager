from firebase_admin import firestore

def get_db():
    return firestore.client()  # יוצרת חיבור ל-Firestore רק כשניגשים לפונקציה

class UserModel:
    @staticmethod
    def create_user(user_id, app_id, user_data):
        db = get_db()
        user_ref = db.collection('users').document(user_id)
        app_data = user_ref.collection('app_data').document(app_id)
        app_data.set(user_data)

    @staticmethod
    def get_user_data(user_id, app_id):
        db = get_db()
        user_ref = db.collection('users').document(user_id)
        app_data = user_ref.collection('app_data').document(app_id).get()
        return app_data.to_dict() if app_data.exists else None

    @staticmethod
    def update_user_data(user_id, app_id, user_data):
        db = get_db()
        user_ref = db.collection('users').document(user_id)
        app_data = user_ref.collection('app_data').document(app_id)
        app_data.update(user_data)

    @staticmethod
    def delete_user_data(user_id, app_id):
        db = get_db()
        user_ref = db.collection('users').document(user_id)
        app_data = user_ref.collection('app_data').document(app_id)
        app_data.delete()