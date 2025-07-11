from app import db 

class Emprestimo(db.Model):
    __tablename__ = 'emprestimos'

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    taxa_juros = db.Column(db.Float, nullable=False)
    parcelas = db.Column(db.Integer, nullable=False)
    data_contrato = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Emprestimo {self.id} valor={self.valor}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'valor': self.valor,
            'taxa_juros': self.taxa_juros,
            'parcelas': self.parcelas,
            'data_contrato': self.data_contrato.isoformat()
        }