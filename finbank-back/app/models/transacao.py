from app import db 

class Transacao(db.Model):
    __tablename__ = 'transacoes'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)  # 'deposito', 'saque', 'transferencia'
    valor = db.Column(db.Float, nullable=False)
    data_hora = db.Column(db.DateTime, server_default=db.func.now())
    conta_remetente_id = db.Column(db.Integer, db.ForeignKey('contas.id'), nullable=False)
    conta_destinatario_id = db.Column(db.Integer, db.ForeignKey('contas.id'), nullable=True)

    def __repr__(self):
        return f'<Transacao {self.id} tipo={self.tipo} valor={self.valor}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'valor': self.valor,
            'data_hora': self.data_hora.isoformat(),
            'conta_remetente_id': self.conta_remetente_id,
            'conta_destinatario_id': self.conta_destinatario_id
        }
    def save(self):
        db.session.add(self)
        db.session.commit()