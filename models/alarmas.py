from utils.db import db

class Alarma(db.Model):
    id_alarma = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    hora_inicio = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=False)

    def __init__(self, nombre, hora_inicio, estado):
        self.nombre = nombre
        self.hora_inicio = hora_inicio
        self.estado = estado