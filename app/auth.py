from flask import request, jsonify
import firebase_admin
from firebase_admin import auth

def authenticate_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token['uid']
    except Exception as e:
        return None