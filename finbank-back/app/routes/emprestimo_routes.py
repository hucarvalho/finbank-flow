from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity  
from app.controllers import emprestimo_controller, conta_controller

emprestimo_bp = Blueprint('emprestimo', __name__, url_prefix='/api/emprestimo')


# Criar um empréstimo
@emprestimo_bp.route('/', methods=['POST'])
@jwt_required()
def criar_emprestimo():
    data = request.get_json()
    user = get_jwt_identity()
    if not data or not data.get('valor') or not data.get('taxa_juros') or not data.get('parcelas'):
        return jsonify({"error": "Dados inválidos"}), 400
    try:
        emprestimo = emprestimo_controller.criar_emprestimo(data, user)
        # Adicionar o valor do emprestimo a conta do usuario 
        conta = conta_controller.get_conta(user)
        conta_controller.adicionar_saldo(conta.id, float(data.get('valor')))
        return jsonify(emprestimo.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    