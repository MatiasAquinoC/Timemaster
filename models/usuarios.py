from flask_login import UserMixin
from utils.db import db

class Usuario(db.Model, UserMixin):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100))
    contrasena = db.Column(db.String(100))

    def __init__(self, nombre, email, contrasena):
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena

    def get_id(self):
        return self.id_usuario