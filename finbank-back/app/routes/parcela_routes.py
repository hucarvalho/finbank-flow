from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers import parcela_controller, conta_controller, emprestimo_controller

parcela_bp = Blueprint('parcela', __name__, url_prefix='/api/parcela')


# Calcular valor da parcela, com base no dia do pagamento
# rota get, passando o id do emprestimo
@parcela_bp.route('/<int:emprestimo_id>', methods=['PATCH'])
@jwt_required()
def pagar_parcela(emprestimo_id):
    user = get_jwt_identity()
    try:
        

        parcela = parcela_controller.calcular_parcela(emprestimo_id, user)

        if not parcela:
        
            return jsonify({"error": "Parcela não encontrada"}), 404
        


        # Atualiza o saldo da conta do usuário
        conta = conta_controller.get_conta(user)

        # verificar se o usuario tem saldo suficiente

        if conta.saldo < parcela.valor:
            return jsonify({"error": "Saldo insuficiente para pagar a parcela"}), 400
        
        parcela_controller.pagar_parcela(emprestimo_id)



        conta_controller.subtrair_saldo(conta.id, parcela.valor)
        
        return jsonify(parcela.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@parcela_bp.route('/<int:emprestimo_id>', methods=['GET'])
@jwt_required()
def calcular_pacela(emprestimo_id):
    user = get_jwt_identity()
    try:
        parcela = parcela_controller.calcular_parcela(emprestimo_id, user)
        if not parcela:
            return jsonify({"error": "Parcela não encontrada"}), 404
        
        # Caso o valor da parcela tenha sido atualizado, acrescer o valor
        # acrescido a parcela ao valor total do emprestimo
        emprestimo = emprestimo_controller.get_by_id(emprestimo_id)
        if emprestimo:
            emprestimo.valor += parcela.valor - parcela.valor_inicial
            emprestimo.save()
        return jsonify(parcela.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500