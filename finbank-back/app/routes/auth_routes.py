from flask import Blueprint, request, jsonify
import sys
import os 
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'controllers')))

from app.controllers import user_controller


auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password') or not data.get('email') or not data.get('cpf') or not data.get('dt_nascimento'):
        return jsonify({"error": "Missing required fields"}), 400
    if not user_controller.check_email(data['email']):
        return jsonify({"error": "Email already exists"}), 400
    return user_controller.register_user(data)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing required fields"}), 400
    user = user_controller.login(data['email'], data['password'])
    if not user:
        return jsonify({"error": "Authentication error"}), 404
    
    return jsonify(user), 200
    


    
    

