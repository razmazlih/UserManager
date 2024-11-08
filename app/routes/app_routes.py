from flask import Blueprint, render_template

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def admin_index():
    return render_template("index.html")

@app_routes.route('/admin')
def index():
    return render_template("admin.html")