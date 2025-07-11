from flask import jsonify
from app.models.user import User
from flask_jwt_extended import create_access_token




def login(email, password):
    try:
        user = User.query.filter_by(email=email).first()
        if user:
            if user.check_password(password):
                access_token = create_access_token(identity=user.id)
                return {
                    "access_token": access_token,
                    "user": user.to_dict()
                }
                
        return None
    except Exception as e:
        raise Exception(f"Erro ao verificar usuário: {str(e)}")

def check_email(email):
    try:
        user = User.query.filter_by(email=email).first()
        if user:
            return False
        return True
    except Exception as e:
        raise Exception(f"Erro ao verificar email: {str(e)}")
    
def register_user(data):
    try:
        new_user = User(
            username=data['username'],
            email=data['email'],
            cpf=data['cpf'],
            dt_nascimento=data['dt_nascimento'],
            telefone=data.get('telefone', None),            
        )
        new_user.set_password(data['password'])
        
        # criar o usuario 
        new_user.save()  
        return jsonify({"message": "Usuário registrado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": f"Erro ao registrar usuário: {str(e)}"}), 500