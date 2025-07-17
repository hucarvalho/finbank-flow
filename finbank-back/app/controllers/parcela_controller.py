from app import db 
from app.models.parcela import Parcela
from datetime import timedelta

def criar_parcelas(emprestimo):
    try:
        parcelas = []
        emprestimo.valor = emprestimo.valor * (1 + emprestimo.taxa_juros / 100)  
        valor_parcela = emprestimo.valor / emprestimo.parcelas
        for i in range(1, emprestimo.parcelas + 1):
            parcela = Parcela(
                valor=valor_parcela,
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