from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.CreateDatabase import Contador  # Asegúrate de importar el modelo y la base de datos

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

class contador:
    def create_contador(nombre, fechaInicio, fechaFin, ID_Usuario):
        nuevo_contador = Contador(nombre=nombre, fechaInicio=fechaInicio, fechaFin=fechaFin, ID_Usuario=ID_Usuario)
        session.add(nuevo_contador)
        session.commit()
        return nuevo_contador

    def get_contador_by_id(contador_id):
        return session.query(Contador).filter(Contador.ID_Conteo == contador_id).first()

    def update_contador(contador_id, nombre=None, fechaInicio=None, fechaFin=None, ID_Usuario=None):
        contador = session.query(Contador).filter(Contador.ID_Conteo == contador_id).first()
        if contador:
            if nombre:
                contador.nombre = nombre
            if fechaInicio:
                contador.fechaInicio = fechaInicio
            if fechaFin:
                contador.fechaFin = fechaFin
            if ID_Usuario:
                contador.ID_Usuario = ID_Usuario
            session.commit()
        return contador
    def delete_contador(contador_id):
        contador = session.query(Contador).filter(Contador.ID_Conteo == contador_id).first()
        if contador:
            session.delete(contador)
            session.commit()
            return None
        return contador
def close_session():
    session.close()
