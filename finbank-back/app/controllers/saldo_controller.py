from flask import jsonify


def depositar(valor):
    try:
        # Simulate depositing to a database or service
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        # Here you would typically update the saldo in a database
        return {"message": "Depósito realizado com sucesso"}
    except Exception as e:
        raise Exception(f"Erro ao realizar depósito: {str(e)}")

def get_saldo():
    try:
        # Simulate fetching saldo from a database or service
        saldo = 1000.00  # Example static value
        return saldo
    except Exception as e:
        raise Exception(f"Erro ao obter saldo: {str(e)}")