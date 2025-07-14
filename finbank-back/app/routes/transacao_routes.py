from app.controllers import transacao_controller, conta_controller, user_controller
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify


transacao_bp = Blueprint('transacao', __name__, url_prefix='/api/transacao')





# Criar uma transação (deposito)


@transacao_bp.route('/teste', methods=['GET'])
def teste_trazer_user_com_contas():
    try:
        user = user_controller.get_user_with_contas_by_cpf("24006282893")
        if user:
            return jsonify(user), 200
        return jsonify({"error": "Usuário não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@transacao_bp.route('/deposito', methods=['POST'])
@jwt_required()
def create_deposito():
    data = request.get_json()
    if not data or not data.get('valor') or not data.get('cpf') or not data.get('agencia') or not data.get('conta') or not data.get('digito') or not data.get('tipo'):
        return jsonify({"error": "Dados inválidos"}), 400
    user_id = get_jwt_identity()
    try:
        # verifica se o usuario tem uma conta
        conta = conta_controller.get_conta(user_id)
        if not conta:
            return jsonify({"error": "Conta não encontrada"}), 404
        # realizar transação
        if data['valor'] <= 0:
            return jsonify({"error": "Valor inválido"}), 400
        # verifica cpf digitado 
        user_com_conta = user_controller.get_user_with_contas_by_cpf(data['cpf'])
        if not user_com_conta:
            return jsonify({"error": "CPF inválido"}), 404
        
        conta_destinatario = user_com_conta['contas'][0]
        # retorna a conta do destinatário para teste
        # return jsonify(conta_destinatario), 200
        if data['agencia'] != conta_destinatario.get('agencia') or data['conta'] != conta_destinatario.get('conta') or data['digito'] != conta_destinatario.get('digito'):
            return jsonify({"error": "Dados da conta inválidos"}), 400

        # verifica se o saldo é suficiente
        if conta.saldo < data.get('valor', 0):
            return jsonify({"error": "Saldo insuficiente"}), 400
        
        #verifica se a conta é a mesma
        if conta.id == conta_destinatario['id']:
            return jsonify({"error": "Não é possível depositar na própria conta"}), 400
        
        data['tipo'] = "deposito"
        transacao = transacao_controller.create_transacao(data, conta.id, conta_destinatario['id'])
        # atualizar saldo da conta
        conta_controller.subtrair_saldo(conta.id, data['valor'])
        conta_controller.adicionar_saldo(conta_destinatario['id'], data['valor'])
        return jsonify(transacao_controller.get_infos_by_id(transacao.id)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Criar uma transação (pix)
@transacao_bp.route('/pix', methods=['POST'])
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
