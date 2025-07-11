from app import db

class Conta(db.Model):
    __tablename__ = 'contas'

    id = db.Column(db.Integer, primary_key=True)
    agencia = db.Column(db.String(20), nullable=False)
    conta = db.Column(db.String(20), nullable=False)
    digito = db.Column(db.String(5), nullable=False)
    saldo = db.Column(db.Float, default=0.0)
    tipo = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    chave_pix = db.Column(db.String(100), nullable=True)
    # relação com o usuario 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Conta {self.agencia}-{self.conta}-{self.digito}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'agencia': self.agencia,
            'conta': self.conta,
            'digito': self.digito,
            'saldo': self.saldo,
            'tipo': self.tipo,
            'created_at': self.created_at.isoformat(),
            'chave_pix': self.chave_pix,
            'user_id': self.user_id
        }
    def save(self):
        db.session.add(self)
        db.session.commit()