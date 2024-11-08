from firebase_admin import firestore

def get_db():
    return firestore.client()

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

        if not app_data.exists:
            return None

        data = app_data.to_dict()
        if 'password' in data:
            del data['password']

        return data

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