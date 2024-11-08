from flask import Blueprint, request, jsonify
from app.auth import authenticate_admin
from app.models.token_model import TokenModel

admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/admin/token', methods=['GET'])
def get_all_tokens():
    if not authenticate_admin(request.headers.get("Admin-Token")):
        return jsonify({"error": "Unauthorized"}), 401

    tokens = TokenModel.get_tokens()
    return jsonify(tokens), 200

@admin_routes.route('/admin/token', methods=['POST'])
def add_token():
    if not authenticate_admin(request.headers.get("Admin-Token")):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    app_id = data.get("app_id")
    token = data.get("token")
    TokenModel.add_token(app_id, token)
    return jsonify({"message": "Token added successfully"}), 201

@admin_routes.route('/admin/token/<app_id>', methods=['PUT'])
def update_token(app_id):
    if not authenticate_admin(request.headers.get("Admin-Token")):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    token = data.get("token")
    TokenModel.update_token(app_id, token)
    return jsonify({"message": "Token updated successfully"}), 200

@admin_routes.route('/admin/token/<app_id>', methods=['DELETE'])
def delete_token(app_id):
    if not authenticate_admin(request.headers.get("Admin-Token")):
        return jsonify({"error": "Unauthorized"}), 401

    TokenModel.delete_token(app_id)
    return jsonify({"message": "Token deleted successfully"}), 200