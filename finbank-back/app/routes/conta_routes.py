from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from app.controllers import conta_controller

conta_bp = Blueprint('conta', __name__, url_prefix='/api/conta')


# buscar conta do usuario
@conta_bp.route('/', methods=['GET'])
@jwt_required()
def get_conta():
    user_id = get_jwt_identity()
    try:
        conta = conta_controller.get_conta(user_id)
        if conta:
            return jsonify(conta.to_dict()), 200
        else:
            return jsonify({"message": "Conta não encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#criar conta do usuario
@conta_bp.route('/', methods=['POST'])
@jwt_required()
def create_conta():
    data = request.get_json()
    user_id = get_jwt_identity()
    try:
        conta = conta_controller.create_conta(data, user_id)
        return jsonify(conta.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

#definir chave pix da conta
@conta_bp.route('/chave-pix', methods=['PUT'])
@jwt_required()
def update_chave_pix():
    data = request.get_json()
    user_id = get_jwt_identity()
    try:
        conta = conta_controller.update_chave_pix(data, user_id)
        return jsonify(conta.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400






