# Exemplo de um model em um lugar diferente [auth]
from delivery.ext.db import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.Unicode, unique=True)
    passwd = db.Column('passwd', db.Unicode)
    admin = db.Column('admin', db.Boolean)
    
    def __repr__(self):
        return self.email
