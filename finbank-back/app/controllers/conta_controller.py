from flask import jsonify
from app.models.conta import Conta
from faker import Faker 

faker = Faker()


def adicionar_saldo(conta_id, valor):
    try:
        conta = Conta.query.get(conta_id)
        if not conta:
            raise ValueError("Conta não encontrada")
        conta.saldo += valor
        conta.save()
        return conta
    except Exception as e:
        raise ValueError(f"Erro ao adicionar saldo: {str(e)}")


def subtrair_saldo(conta_id, valor):
    try:
        conta = Conta.query.get(conta_id)
        if not conta:
            raise ValueError("Conta não encontrada")
        if conta.saldo < valor:
            raise ValueError("Saldo insuficiente")
        conta.saldo -= valor
        conta.save()
        return conta
    except Exception as e:
        raise ValueError(f"Erro ao subtrair saldo: {str(e)}")

def get_conta_by_chave_pix(chave_pix):
    try:
        conta = Conta.query.filter_by(chave_pix=chave_pix).first()
        if not conta:
            raise ValueError("Conta não encontrada para a chave PIX fornecida")
        return conta
    except Exception as e:
            raise ValueError(f"Erro ao buscar conta por chave PIX: {str(e)}")

            
def get_conta(user_id):
    try:
        conta = Conta.query.filter_by(user_id=user_id).first()
        if not conta:
            raise ValueError("Conta não encontrada para o usuário")
        return conta
    except Exception as e:
        raise ValueError(f"Erro ao buscar conta: {str(e)}")

def create_conta(data, user_id):
    try:
        
        agencia = data.get('agencia', faker.bothify("####-#"))
        conta = data.get('conta', faker.bothify("#####"))
        digito = data.get('digito', faker.random_digit_not_null())
        tipo = data.get('tipo', 'corrente')  
        
        new_conta = Conta(
            agencia=agencia,
            conta=conta,
            digito=digito,
            tipo=tipo,
            user_id=user_id
        )
        
        new_conta.save()
        return new_conta
    except Exception as e:
        raise Exception(f"Erro ao criar conta: {str(e)}")

def update_chave_pix(data, user_id):
    try:
        chave_pix = data.get('chave_pix')
        if not chave_pix:
            raise ValueError("Chave PIX não pode ser vazia")
        conta = Conta.query.filter_by(user_id=user_id).first()
        if not conta:
            raise ValueError("Conta não encontrada para o usuário")
        conta.chave_pix = chave_pix
        conta.save()
        return conta
    except Exception as e:
        raise Exception(f"Erro ao atualizar chave PIX: {str(e)}")