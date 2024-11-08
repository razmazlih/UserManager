from flask import Blueprint, request, jsonify
from app.auth import authenticate_token
from app.models.user_model import UserModel

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/user', methods=['POST'])
def create_user():
    token = request.headers.get('Authorization')
    app_id = authenticate_token(token)
    if not app_id:
        return jsonify({"error": "Unauthorized"}), 401

    user_data = request.get_json()
    user_id = user_data.get("phone_number")
    UserModel.create_user(user_id, app_id, user_data)
    return jsonify({"message": "User created successfully"}), 201

@user_routes.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    token = request.headers.get('Authorization')
    app_id = authenticate_token(token)
    if not app_id:
        return jsonify({"error": "Unauthorized"}), 401

    user_data = UserModel.get_user_data(user_id, app_id)
    if user_data:
        return jsonify(user_data), 200
    return jsonify({"error": "User not found"}), 404

@user_routes.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    token = request.headers.get('Authorization')
    app_id = authenticate_token(token)
    if not app_id:
        return jsonify({"error": "Unauthorized"}), 401

    user_data = request.get_json()
    UserModel.update_user_data(user_id, app_id, user_data)
    return jsonify({"message": "User updated successfully"}), 200

@user_routes.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    token = request.headers.get('Authorization')
    app_id = authenticate_token(token)
    if not app_id:
        return jsonify({"error": "Unauthorized"}), 401

    UserModel.delete_user_data(user_id, app_id)
    return jsonify({"message": "User deleted successfully"}), 200