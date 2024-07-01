from utils.db import db

class Pomodoro(db.Model):
    id_pomodoro = db.Column(db.Integer, primary_key = True)
    duracion_trabajo = db.Column(db.Integer)
    duracion_descanso = db.Column(db.Integer)

    def __init__(self, duracion_trabajo, duracion_descanso):
        self.duracion_trabajo = duracion_trabajo
        self.duracion_descanso = duracion_descanso