from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from . import config 
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


jwt = JWTManager()


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    from .routes import saldo_routes, auth_routes, conta_routes, transacao_routes
    app.register_blueprint(saldo_routes.bp)
    app.register_blueprint(auth_routes.auth_bp)
    app.register_blueprint(conta_routes.conta_bp)
    app.register_blueprint(transacao_routes.transacao_bp)


    from app.models import user, conta, transacao, emprestimo, parcela, log


    return app