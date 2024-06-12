from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.createDatabase import Alarma  # Asegúrate de importar el modelo y la base de datos

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

class alarma:
    def create_alarma(nombre, horaInicio, estado, sonido, ID_Usuario):
        nueva_alarma = Alarma(nombre=nombre, horaInicio=horaInicio, estado=estado, sonido=sonido, ID_Usuario=ID_Usuario)
        session.add(nueva_alarma)
        session.commit()

    def get_alarma_by_id(alarma_id):
        return session.query(Alarma).filter(Alarma.ID_Alarma == alarma_id).first()

    def update_alarma(alarma_id, nombre=None, horaInicio=None, estado=None, sonido=None, ID_Usuario=None):
        alarma = session.query(Alarma).filter(Alarma.ID_Alarma == alarma_id).first()
        if alarma:
            if nombre:
                alarma.nombre = nombre
            if horaInicio:
                alarma.horaInicio = horaInicio
            if estado is not None:
                alarma.estado = estado
            if sonido:
                alarma.sonido = sonido
            if ID_Usuario:
                alarma.ID_Usuario = ID_Usuario
            session.commit()

    def delete_alarma(alarma_id):
        alarma = session.query(Alarma).filter(Alarma.ID_Alarma == alarma_id).first()
        if alarma:
            session.delete(alarma)
            session.commit()

def close_session():
    session.close()
