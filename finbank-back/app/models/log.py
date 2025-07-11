from app import db 

class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.DateTime, server_default=db.func.now())
    tipo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    tabela_afetada = db.Column(db.String(50), nullable=False)
    referencia_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)


    def __repr__(self):
        return super().__repr__()
    
    def to_dict(self):
        return {
            'id': self.id,
            'data_hora': self.data_hora.isoformat(),
            'tipo': self.tipo,
            'descricao': self.descricao,
            'tabela_afetada': self.tabela_afetada,
            'referencia_id': self.referencia_id,
            'user_id': self.user_id
        }
