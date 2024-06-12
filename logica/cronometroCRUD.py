from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelo.createDatabase import Cronometro, Base  # Asegúrate de importar el modelo y la base de datos

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

class cronometro:
    def create_cronometro(fechaInicio, duracion, fechasParciales, ID_Usuario):
        nuevo_cronometro = Cronometro(fechaInicio=fechaInicio, duracion=duracion, fechasParciales=fechasParciales, ID_Usuario=ID_Usuario)
        session.add(nuevo_cronometro)
        session.commit()

    def get_cronometro_by_id(cronometro_id):
        return session.query(Cronometro).filter(Cronometro.ID_Cronometro == cronometro_id).first()

    def update_cronometro(cronometro_id, fechaInicio=None, duracion=None, fechasParciales=None, ID_Usuario=None):
        cronometro = session.query(Cronometro).filter(Cronometro.ID_Cronometro == cronometro_id).first()
        if cronometro:
            if fechaInicio:
                cronometro.fechaInicio = fechaInicio
            if duracion:
                cronometro.duracion = duracion
            if fechasParciales:
                cronometro.fechasParciales = fechasParciales
            if ID_Usuario:
                cronometro.ID_Usuario = ID_Usuario
            session.commit()

    def delete_cronometro(cronometro_id):
        cronometro = session.query(Cronometro).filter(Cronometro.ID_Cronometro == cronometro_id).first()
        if cronometro:
            session.delete(cronometro)
            session.commit()

def close_session():
    session.close()
