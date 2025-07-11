from app.models.transacao import Transacao
from app import db


def get_infos_by_id(transacao_id):
    try:
        sql = db.text("""
                    select t.data_hora, t.valor, r.username as remetente, d.username as destinatario FROM transacoes as t
                    join contas ct
                    on ct.id = t.conta_remetente_id
                    join contas cd
                    on cd.id = conta_destinatario_id
                    join users r
                    on r.id = ct.user_id
                    join users d
                    on d.id = cd.user_id
                    where t.id = :transacao_id;
                   """)
        result = db.session.execute(sql, {'transacao_id': transacao_id}).fetchone()
        if result:
            return {
                'data_hora': result[0].strftime('%Y-%m-%d %H:%M:%S'),
                'valor': result[1],
                'remetente': result[2],
                'destinatario': result[3]
            }
        else:
            raise ValueError("Transação não encontrada")
    except Exception as e:
        raise ValueError(f"Erro ao buscar informações da transação: {str(e)}")

def create_transacao(data, conta_remetente_id, conta_destinatario_id):
    try:
        tipo = data.get('tipo', 'transferencia')
        valor = data.get('valor')
        
        transacao = Transacao(
            tipo=tipo,
            valor=valor,
            conta_remetente_id=conta_remetente_id,
            conta_destinatario_id=conta_destinatario_id
        )
        transacao.save()
        return transacao
    except Exception as e:
        raise Exception(f"Erro ao criar transação: {str(e)}")

