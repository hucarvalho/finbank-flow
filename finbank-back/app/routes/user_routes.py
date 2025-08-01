from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers import user_controller

user_bp = Blueprint('user', __name__, url_prefix='/api/user')

@user_bp.route('/history', methods=['GET'])
@jwt_required()
def get_user_history():
    user = get_jwt_identity()
    try:
        history = user_controller.get_user_history(user)
        return jsonify(history), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500