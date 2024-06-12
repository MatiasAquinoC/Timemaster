from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelo.createDatabase import Pomodoro, Base  # Asegúrate de importar el modelo y la base de datos

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

class pomodoro:
    def create_pomodoro(duracionTrabajo, horaInicio, duracionDescanso, estado, ID_Usuario):
        nuevo_pomodoro = Pomodoro(duracionTrabajo=duracionTrabajo, horaInicio=horaInicio, duracionDescanso=duracionDescanso, estado=estado, ID_Usuario=ID_Usuario)
        session.add(nuevo_pomodoro)
        session.commit()

    def get_pomodoro_by_id(pomodoro_id):
        return session.query(Pomodoro).filter(Pomodoro.ID_Pomodoro == pomodoro_id).first()

    def update_pomodoro(pomodoro_id, duracionTrabajo=None, horaInicio=None, duracionDescanso=None, estado=None, ID_Usuario=None):
        pomodoro = session.query(Pomodoro).filter(Pomodoro.ID_Pomodoro == pomodoro_id).first()
        if pomodoro:
            if duracionTrabajo:
                pomodoro.duracionTrabajo = duracionTrabajo
            if horaInicio:
                pomodoro.horaInicio = horaInicio
            if duracionDescanso:
                pomodoro.duracionDescanso = duracionDescanso
            if estado is not None:
                pomodoro.estado = estado
            if ID_Usuario:
                pomodoro.ID_Usuario = ID_Usuario
            session.commit()

    def delete_pomodoro(pomodoro_id):
        pomodoro = session.query(Pomodoro).filter(Pomodoro.ID_Pomodoro == pomodoro_id).first()
        if pomodoro:
            session.delete(pomodoro)
            session.commit()
def close_session():
    session.close()
