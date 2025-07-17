from app import db
from passlib.hash import bcrypt

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    dt_nascimento = db.Column(db.Date, nullable=False)
    telefone = db.Column(db.String(15), nullable=True)
    renda = db.Column(db.Float, default=0.0)

    #relação com a conta 
    contas = db.relationship('Conta', backref='user', lazy=True)
    # emprestimos = db.relationship('Emprestimo', backref='user', lazy=True)
    

    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'cpf': self.cpf,
            'dt_nascimento': self.dt_nascimento, 
            'telefone': self.telefone,
            'renda': self.renda
        }
    
    def to_dict_with_contas(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'cpf': self.cpf,
            'dt_nascimento': self.dt_nascimento, 
            'telefone': self.telefone,
            'renda': self.renda,
            'contas': [conta.to_dict() for conta in self.contas]
        }
    
    def set_password(self, password):
        self.password = bcrypt.hash(password)

    def check_password(self, password):
        return bcrypt.verify(password, self.password)

    def save(self):
        db.session.add(self)
        db.session.commit()