from app import db 
from app.models.parcela import Parcela
from datetime import timedelta, datetime


def calcular_parcela(emprestimo_id, user):
    try:
        # Pegar primeira parcela não paga da data mais proxima

        parcela = Parcela.query.filter(
            Parcela.emprestimo_id == emprestimo_id,
            Parcela.status != 'paga'
            ).order_by(Parcela.data_vencimento).first()
        if not parcela:
            raise Exception("Parcela não encontrada")
        data_atual = datetime.today()
        if parcela.data_vencimento < data_atual:
            # Acrescer ao valor da parcela a taxa de juros
            parcela.valor += parcela.valor * (parcela.taxa_juros / 100)
            parcela.status = 'atrasada'
            parcela.save()
        return parcela
    except Exception as e:
        raise Exception(f"Erro ao calcular parcela: {str(e)}")

def criar_parcelas(emprestimo):
    try:
        parcelas = []
        emprestimo.valor = emprestimo.valor * (1 + emprestimo.taxa_juros / 100)  
        emprestimo.valor_inicial = emprestimo.valor  
        valor_parcela = emprestimo.valor / emprestimo.parcelas
        for i in range(1, emprestimo.parcelas + 1):
            parcela = Parcela(
                valor=valor_parcela,
                valor_inicial=valor_parcela,
                data_vencimento=emprestimo.data_contrato + timedelta(days=i * 30),  # Exemplo: vencimento mensal
                taxa_juros=emprestimo.taxa_juros,
                status='pendente',
                emprestimo_id=emprestimo.id
            )
            parcelas.append(parcela)
        
        db.session.bulk_save_objects(parcelas)
        db.session.commit()
        return parcelas
    except Exception as e:
        raise Exception(f"Erro ao criar parcelas: {str(e)}")