from flask import Flask, request, g 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from . import config 
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


import time 
import logging







jwt = JWTManager()


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    logger = logging.getLogger('performance')
    
   
    CORS(app)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    from .routes import saldo_routes, auth_routes, conta_routes, transacao_routes, emprestimo_routes, parcela_routes, user_routes
    app.register_blueprint(user_routes.user_bp)
    app.register_blueprint(saldo_routes.bp)
    app.register_blueprint(auth_routes.auth_bp)
    app.register_blueprint(conta_routes.conta_bp)
    app.register_blueprint(transacao_routes.transacao_bp)
    app.register_blueprint(emprestimo_routes.emprestimo_bp)
    app.register_blueprint(parcela_routes.parcela_bp)
    
    from app.models import user, conta, transacao, emprestimo, parcela, log
    from app.models.log import Log

    @app.before_request
    def start_timer():
        g.start = time.time()

    @app.after_request
    def log_request(response):
        if hasattr(g, 'start'):
            duration = time.time() - g.start
            method = request.method
            path = request.path
            status = response.status


            logger.info(f"{method} {path} - {status} - {duration:.2f}s")

            try:
                log = Log(
                    method=method,
                    path=path,
                    duration=duration,
                    status_code=status
                )
                log.save()
            except Exception as e:
                logger.error(f"Failed to log request: {e}")
        return response


    return app