from app import db 
from datetime import datetime

class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(10), nullable=False)
    path = db.Column(db.Text)
    duration = db.Column(db.Float)
    status_code = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return super().__repr__()
    
    def to_dict(self):
        return {
            'id': self.id,
            'method': self.method,
            'path': self.path,
            'duration': self.duration,
            'status_code': self.status_code,
            'created_at': self.created_at.isoformat()
        }

    def save(self):
        db.session.add(self)
        db.session.commit()