from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.CreateDatabase import Temporizador  # Asegúrate de importar el modelo y la base de datos

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

class temporizador:
    def create_temporizador(FechaInicio, duracion, sonido, ID_Usuario):
        nuevo_temporizador = Temporizador(FechaInicio=FechaInicio, duracion=duracion, sonido=sonido, ID_Usuario=ID_Usuario)
        session.add(nuevo_temporizador)
        session.commit()
        return nuevo_temporizador
    def get_temporizador_by_id(temporizador_id):
        return session.query(Temporizador).filter(Temporizador.ID_Temporizador == temporizador_id).first()


    def update_temporizador(temporizador_id, FechaInicio=None, duracion=None, sonido=None, ID_Usuario=None):
        temporizador = session.query(Temporizador).filter(Temporizador.ID_Temporizador == temporizador_id).first()
        if temporizador:
            if FechaInicio:
                temporizador.FechaInicio = FechaInicio
            if duracion:
                temporizador.duracion = duracion
            if sonido:
                temporizador.sonido = sonido
            if ID_Usuario:
                temporizador.ID_Usuario = ID_Usuario
            session.commit()
        return temporizador
    def delete_temporizador(temporizador_id):
        temporizador = session.query(Temporizador).filter(Temporizador.ID_Temporizador == temporizador_id).first()
        if temporizador:
            session.delete(temporizador)
            session.commit()
            return None
        return temporizador
def close_session():
    session.close()
