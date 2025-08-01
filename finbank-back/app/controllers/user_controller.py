from flask import jsonify
from app.models.user import User
from flask_jwt_extended import create_access_token
from app import db


def get_user_history(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "Usuário não encontrado"}), 404
        
        sql = db.text(f"""
                    select transacoes.id, data_hora, valor, case when conta_remetente_id = {user_id} then 'transacao feita' when conta_destinatario_id = {user_id} then 'transação recebida' else 'nok' end as tipo from transacoes
                    join contas
                    on (contas.id = transacoes.conta_remetente_id or contas.id = transacoes.conta_destinatario_id) and contas.user_id = {user_id}

                    union

                    select e.id, data_contrato, valor_entregue, 'emprestimo' as tipo from emprestimos as e
                    where user_id = {user_id}

                    union

                    select p.id, data_pagamento, p.valor, 'parcela' as tipo from parcelas as p
                    join emprestimos e
                    on e.id = p.emprestimo_id
                    where e.user_id = {user_id} and status = 'paga' """)
        result = db.session.execute(sql).fetchall()
        history = []
        for row in result:
            history.append({
                'id': row[0],
                'data_hora': row[1].strftime('%Y-%m-%d %H:%M:%S'),
                'valor': row[2],
                'tipo': row[3]
            })
        return history
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_user_with_contas_by_cpf(cpf):
    try:
        user = User.query.filter_by(cpf=cpf).first()
        if user:
            return user.to_dict_with_contas()
        return None
    except Exception as e:
        raise Exception(f"Erro ao buscar usuário: {str(e)}")

def login(email, password):
    try:
        user = User.query.filter_by(email=email).first()
        print(user)
        if user:
            if user.check_password(password):
                access_token = create_access_token(identity=str(user.id))
                return {
                    "access_token": access_token,
                    "user": user.to_dict()
                }
                
        return None
    except Exception as e:
        raise Exception(f"Erro ao verificar usuário: {str(e)}")

def check_email(email):
    try:
        user = User.query.filter_by(email=email).first()
        if user:
            return False
        return True
    except Exception as e:
        raise Exception(f"Erro ao verificar email: {str(e)}")
    
def register_user(data):
    try:
        new_user = User(
            username=data['username'],
            email=data['email'],
            cpf=data['cpf'],
            dt_nascimento=data['dt_nascimento'],
            telefone=data.get('telefone', None),            
        )
        new_user.set_password(data['password'])
        
        # criar o usuario 
        new_user.save()  
        return jsonify({"message": "Usuário registrado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": f"Erro ao registrar usuário: {str(e)}"}), 500