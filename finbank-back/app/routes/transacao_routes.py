from app.controllers import transacao_controller, conta_controller
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify


transacao_bp = Blueprint('transacao', __name__, url_prefix='/api/transacao')

# Criar uma transação (pix)
@transacao_bp.route('/', methods=['POST'])
@jwt_required()
def create_transacao():
    data = request.get_json()
    if not data or not data.get('valor') or not data.get('chave_pix'):
        return jsonify({"error": "Dados inválidos"}), 400
    user_id = get_jwt_identity()
    try:
        # verifica se o usuario tem uma conta
        conta = conta_controller.get_conta(user_id)
        if not conta:
            return jsonify({"error": "Conta não encontrada"}), 404
        #verifica se o saldo é suficiente
        if conta.saldo < data.get('valor', 0):
            return jsonify({"error": "Saldo insuficiente"}), 400

        # verifica se a chave pix digitada pertence a outra conta
        if 'chave_pix' not in data:
            return jsonify({"error": "Chave PIX do destinatário é obrigatória"}), 400
        conta_destinatario = conta_controller.get_conta_by_chave_pix(data['chave_pix'])
        if not conta_destinatario:
            return jsonify({"error": "Conta destinatária não encontrada"}), 404
        # verifica se a conta é a mesma
        if conta.id == conta_destinatario.id:
            return jsonify({"error": "Não é possível transferir para a própria conta"}), 400
        # realizar transação
        data['tipo'] = "transferência pix"
        transacao = transacao_controller.create_transacao(
            data, 
            conta.id, 
            conta_destinatario.id
        )
        # atualizar saldo das contas
        conta_controller.subtrair_saldo(conta.id, data['valor'])
        conta_controller.adicionar_saldo(conta_destinatario.id, data['valor'])
        return jsonify(transacao_controller.get_infos_by_id(transacao.id)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
