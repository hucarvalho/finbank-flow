from app import db 

class Emprestimo(db.Model):
    __tablename__ = 'emprestimos'

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    taxa_juros = db.Column(db.Float, nullable=False)
    parcelas = db.Column(db.Integer, nullable=False)
    valor_inicial = db.Column(db.Float, nullable=False)  
    valor_entregue = db.Column(db.Float, nullable=False)
    data_contrato = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='emprestimos', lazy=True)

    

    def __repr__(self):
        return f'<Emprestimo {self.id} valor={self.valor}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'valor': self.valor,
            'taxa_juros': self.taxa_juros,
            'parcelas': self.parcelas,
            'data_contrato': self.data_contrato.isoformat(),
            
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()