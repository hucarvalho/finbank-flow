from flask_migrate import Migrate, upgrade
from app import create_app, db

#models 

from app.models.parcela import Parcela
from app.models.transacao import Transacao
from app.models.emprestimo import Emprestimo
from app.models.conta import Conta
from app.models.user import User
from app.models.log import Log




app = create_app()

migrate = Migrate(app, db)
