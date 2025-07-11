from app import db 


class Parcela(db.Model):
    __tablename__ = 'parcelas'

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    data_vencimento = db.Column(db.DateTime, nullable=False)
    taxa_juros = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pendente')  # 'pendente', 'paga', 'atrasada'
    emprestimo_id = db.Column(db.Integer, db.ForeignKey('emprestimos.id'), nullable=False)
    data_pagamento = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Parcela {self.id} valor={self.valor} status={self.status}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'valor': self.valor,
            'data_vencimento': self.data_vencimento.isoformat(),
            'taxa_juros': self.taxa_juros,
            'status': self.status,
            'emprestimo_id': self.emprestimo_id,
            'data_pagamento': self.data_pagamento.isoformat() if self.data_pagamento else None
        }

