from app import db
from app.models.emprestimo import Emprestimo
from app.controllers import parcela_controller


def get_by_id(emprestimo_id):
    try:
        emprestimo = Emprestimo.query.get(emprestimo_id)
        if not emprestimo:
            raise Exception("Empréstimo não encontrado")
        return emprestimo
    except Exception as e:
        raise Exception(f"Erro ao buscar empréstimo: {str(e)}")

def criar_emprestimo(data, user):
    try:
        emprestimo = Emprestimo(
            valor=float(data.get('valor')),
            taxa_juros=float(data.get('taxa_juros')),
            parcelas=float(data.get('parcelas')),
            valor_inicial=float(data.get('valor')),
            valor_entregue=float(data.get('valor')),
            user_id=user
        )
        emprestimo.save()
        parcelas = parcela_controller.criar_parcelas(emprestimo)
        emprestimo.parcelas_info = parcelas  
        return emprestimo
    except Exception as e:
        raise Exception(f"Erro ao criar empréstimo: {str(e)}")