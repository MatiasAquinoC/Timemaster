from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.createDatabase import Configuracion  # Asegúrate de importar el modelo y la base de datos

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

class configuracion:
    def create_configuracion(configuracionModo, configuracionReloj, configuracionFuente, ID_Usuario):
        nueva_configuracion = Configuracion(configuracionModo=configuracionModo, configuracionReloj=configuracionReloj, configuracionFuente=configuracionFuente, ID_Usuario=ID_Usuario)
        session.add(nueva_configuracion)
        session.commit()

    def get_configuracion_by_id(configuracion_id):
        return session.query(Configuracion).filter(Configuracion.ID_Configuracion == configuracion_id).first()

    def update_configuracion(configuracion_id, configuracionModo=None, configuracionReloj=None, configuracionFuente=None, ID_Usuario=None):
        configuracion = session.query(Configuracion).filter(Configuracion.ID_Configuracion == configuracion_id).first()
        if configuracion:
            if configuracionModo is not None:
                configuracion.configuracionModo = configuracionModo
            if configuracionReloj:
                configuracion.configuracionReloj = configuracionReloj
            if configuracionFuente:
                configuracion.configuracionFuente = configuracionFuente
            if ID_Usuario:
                configuracion.ID_Usuario = ID_Usuario
            session.commit()

    def delete_configuracion(configuracion_id):
        configuracion = session.query(Configuracion).filter(Configuracion.ID_Configuracion == configuracion_id).first()
        if configuracion:
            session.delete(configuracion)
            session.commit()
def close_session():
    session.close()
