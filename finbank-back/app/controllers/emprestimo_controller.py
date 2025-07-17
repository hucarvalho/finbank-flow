from app import db
from app.models.emprestimo import Emprestimo
from app.controllers import parcela_controller


def criar_emprestimo(data, user):
    try:
        emprestimo = Emprestimo(
            valor=float(data.get('valor')),
            taxa_juros=float(data.get('taxa_juros')),
            parcelas=float(data.get('parcelas')),
            user_id=user
        )
        emprestimo.save()
        parcelas = parcela_controller.criar_parcelas(emprestimo)
        emprestimo.parcelas_info = parcelas  
        return emprestimo
    except Exception as e:
        raise Exception(f"Erro ao criar empréstimo: {str(e)}")