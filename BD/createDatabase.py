from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    ID_Usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    contraseña = Column(String, nullable=False)
    alarmas = relationship('Alarma', back_populates='usuario')
    pomodoros = relationship('Pomodoro', back_populates='usuario')
    temporizadores = relationship('Temporizador', back_populates='usuario')
    cronometros = relationship('Cronometro', back_populates='usuario')
    configuraciones = relationship('Configuracion', back_populates='usuario')
    contadores = relationship('Contador', back_populates='usuario')

class Alarma(Base):
    __tablename__ = 'alarma'
    ID_Alarma = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    horaInicio = Column(DateTime, nullable=False)
    estado = Column(Boolean, nullable=False)
    sonido = Column(String, nullable=False)
    ID_Usuario = Column(Integer, ForeignKey('usuario.ID_Usuario'), nullable=False)
    usuario = relationship('Usuario', back_populates='alarmas')

class Pomodoro(Base):
    __tablename__ = 'pomodoro'
    ID_Pomodoro = Column(Integer, primary_key=True, autoincrement=True)
    duracionTrabajo = Column(DateTime, nullable=False)
    horaInicio = Column(DateTime, nullable=False)
    duracionDescanso = Column(DateTime, nullable=False)
    estado = Column(Boolean, nullable=False)
    ID_Usuario = Column(Integer, ForeignKey('usuario.ID_Usuario'), nullable=False)
    usuario = relationship('Usuario', back_populates='pomodoros')

class Temporizador(Base):
    __tablename__ = 'temporizador'
    ID_Temporizador = Column(Integer, primary_key=True, autoincrement=True)
    FechaInicio = Column(DateTime, nullable=False)
    duracion = Column(DateTime, nullable=False)
    ID_Usuario = Column(Integer, ForeignKey('usuario.ID_Usuario'), nullable=False)
    sonido = Column(String, nullable=False)
    usuario = relationship('Usuario', back_populates='temporizadores')

class Cronometro(Base):
    __tablename__ = 'cronometro'
    ID_Cronometro = Column(Integer, primary_key=True, autoincrement=True)
    fechaInicio = Column(DateTime, nullable=False)
    duracion = Column(DateTime, nullable=False)
    fechasParciales = Column(DateTime, nullable=False)
    ID_Usuario = Column(Integer, ForeignKey('usuario.ID_Usuario'), nullable=False)
    usuario = relationship('Usuario', back_populates='cronometros')

class Configuracion(Base):
    __tablename__ = 'configuracion'
    ID_Configuracion = Column(Integer, primary_key=True, autoincrement=True)
    configuracionModo = Column(Boolean, nullable=False)
    configuracionReloj = Column(String, nullable=False)
    configuracionFuente = Column(Integer, nullable=False)
    ID_Usuario = Column(Integer, ForeignKey('usuario.ID_Usuario'), nullable=False)
    usuario = relationship('Usuario', back_populates='configuraciones')

class Contador(Base):
    __tablename__ = 'contador'
    ID_Conteo = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    fechaInicio = Column(DateTime, nullable=False)
    fechaFin = Column(DateTime, nullable=False)
    ID_Usuario = Column(Integer, ForeignKey('usuario.ID_Usuario'), nullable=False)
    usuario = relationship('Usuario', back_populates='contadores')

# Configuración de la base de datos
engine = create_engine('sqlite:///mydatabase.db')

# Creación de las tablas
Base.metadata.create_all(engine)

# Creación de una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Inserción de registros en las tablas
# Crear un nuevo usuario
nuevo_usuario = Usuario(nombre='John Doe', email='john@example.com', contraseña='password123')
session.add(nuevo_usuario)
session.commit()

# Crear una nueva alarma para el usuario
nueva_alarma = Alarma(
    nombre='Despertar',
    horaInicio=datetime(2024, 6, 12, 7, 0),
    estado=True,
    sonido='alarma1.mp3',
    ID_Usuario=nuevo_usuario.ID_Usuario
)
session.add(nueva_alarma)
session.commit()

# Crear un nuevo pomodoro para el usuario
nuevo_pomodoro = Pomodoro(
    duracionTrabajo=datetime(2024, 6, 12, 1, 0),
    horaInicio=datetime(2024, 6, 12, 9, 0),
    duracionDescanso=datetime(2024, 6, 12, 0, 15),
    estado=True,
    ID_Usuario=nuevo_usuario.ID_Usuario
)
session.add(nuevo_pomodoro)
session.commit()

# Crear un nuevo temporizador para el usuario
nuevo_temporizador = Temporizador(
    FechaInicio=datetime(2024, 6, 12, 10, 0),
    duracion=datetime(2024, 6, 12, 0, 30),
    sonido='temporizador1.mp3',
    ID_Usuario=nuevo_usuario.ID_Usuario
)
session.add(nuevo_temporizador)
session.commit()

# Crear un nuevo cronometro para el usuario
nuevo_cronometro = Cronometro(
    fechaInicio=datetime(2024, 6, 12, 11, 0),
    duracion=datetime(2024, 6, 12, 0, 45),
    fechasParciales=datetime(2024, 6, 12, 0, 15),
    ID_Usuario=nuevo_usuario.ID_Usuario
)
session.add(nuevo_cronometro)
session.commit()

# Crear una nueva configuración para el usuario
nueva_configuracion = Configuracion(
    configuracionModo=True,
    configuracionReloj='24h',
    configuracionFuente=12,
    ID_Usuario=nuevo_usuario.ID_Usuario
)
session.add(nueva_configuracion)
session.commit()

# Crear un nuevo contador para el usuario
nuevo_contador = Contador(
    nombre='Cuenta regresiva',
    fechaInicio=datetime(2024, 6, 12, 12, 0),
    fechaFin=datetime(2024, 6, 12, 13, 0),
    ID_Usuario=nuevo_usuario.ID_Usuario
)
session.add(nuevo_contador)
session.commit()

print("Base de datos y tablas creadas con éxito")
print("Registros insertados con éxito")
