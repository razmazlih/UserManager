from flask import Blueprint

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    return "Welcome to the User Management Service"