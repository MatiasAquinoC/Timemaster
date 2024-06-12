import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelo.createDatabase import Pomodoro, Base  # Asegúrate de importar el modelo y la base de datos
from logica.pomodoroCRUD import pomodoro  # Asegúrate de importar la clase CRUD para Pomodoro

class TestPomodoroCRUDOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Crear una base de datos en memoria para pruebas
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()
        cls.pomodoro_crud = pomodoro

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def setUp(self):
        # Reiniciar la base de datos antes de cada prueba
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)

    def test_create_pomodoro(self):
        duracionTrabajo = datetime.strptime('2023-06-12 00:25:00', '%Y-%m-%d %H:%M:%S')
        horaInicio = datetime.strptime('2023-06-12 08:00:00', '%Y-%m-%d %H:%M:%S')
        duracionDescanso = datetime.strptime('2023-06-12 00:05:00', '%Y-%m-%d %H:%M:%S')
        estado = True
        ID_Usuario = 1
        self.pomodoro_crud.create_pomodoro(duracionTrabajo, horaInicio, duracionDescanso, estado, ID_Usuario)
        pomodoro = self.session.query(Pomodoro).filter_by(ID_Usuario=ID_Usuario).first()
        self.assertIsNotNone(pomodoro)
        self.assertEqual(pomodoro.duracionTrabajo, duracionTrabajo)

    def test_read_pomodoro(self):
        duracionTrabajo = datetime
