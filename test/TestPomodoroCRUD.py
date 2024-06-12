import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.CreateDatabase import Base, Pomodoro  # Asegúrate de importar el modelo y la base de datos
from src.logica.PomodoroCRUD import pomodoro  # Asegúrate de importar la clase CRUD para Pomodoro

class TestPomodoroCRUDOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.pomodoro_crud = pomodoro

    def setUp(self):
        self.session = self.Session()
        self.pomodoro_crud.session = self.session
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_create_pomodoro(self):
        duracionTrabajo = datetime(2024, 6, 13, 0, 25, 0)
        horaInicio = datetime(2024, 6, 13, 8, 0, 0)
        duracionDescanso = datetime(2024, 6, 13, 0, 5, 0)
        estado = True
        ID_Usuario = 1
        nuevo_pomodoro = self.pomodoro_crud.create_pomodoro(duracionTrabajo, horaInicio, duracionDescanso, estado, ID_Usuario)
        self.session.commit()
        self.assertIsNotNone(nuevo_pomodoro)
        self.assertEqual(nuevo_pomodoro.duracionTrabajo, duracionTrabajo)
        self.assertEqual(nuevo_pomodoro.horaInicio, horaInicio)
        self.assertEqual(nuevo_pomodoro.duracionDescanso, duracionDescanso)
        self.assertTrue(nuevo_pomodoro.estado)
        self.assertEqual(nuevo_pomodoro.ID_Usuario, ID_Usuario)

    def test_get_pomodoro_by_id(self):
        duracionTrabajo = datetime(2024, 6, 13, 0, 25, 0)
        horaInicio = datetime(2024, 6, 13, 8, 0, 0)
        duracionDescanso = datetime(2024, 6, 13, 0, 5, 0)
        estado = True
        ID_Usuario = 1
        nuevo_pomodoro = self.pomodoro_crud.create_pomodoro(duracionTrabajo, horaInicio, duracionDescanso, estado, ID_Usuario)
        self.session.commit()
        fetched_pomodoro = self.pomodoro_crud.get_pomodoro_by_id(nuevo_pomodoro.ID_Pomodoro)
        self.assertIsNotNone(fetched_pomodoro)
        self.assertEqual(fetched_pomodoro.ID_Pomodoro, nuevo_pomodoro.ID_Pomodoro)

    def test_update_pomodoro(self):
        duracionTrabajo = datetime(2024, 6, 13, 0, 25, 0)
        horaInicio = datetime(2024, 6, 13, 8, 0, 0)
        duracionDescanso = datetime(2024, 6, 13, 0, 5, 0)
        estado = True
        ID_Usuario = 1
        nuevo_pomodoro = self.pomodoro_crud.create_pomodoro(duracionTrabajo, horaInicio, duracionDescanso, estado, ID_Usuario)
        self.session.commit()
        updated_pomodoro = self.pomodoro_crud.update_pomodoro(nuevo_pomodoro.ID_Pomodoro, duracionTrabajo=datetime(2024, 6, 13, 0, 30, 0), estado=False)
        self.session.commit()
        self.assertIsNotNone(updated_pomodoro)
        self.assertEqual(updated_pomodoro.duracionTrabajo, datetime(2024, 6, 13, 0, 30, 0))
        self.assertFalse(updated_pomodoro.estado)

    def test_delete_pomodoro(self):
        duracionTrabajo = datetime(2024, 6, 13, 0, 25, 0)
        horaInicio = datetime(2024, 6, 13, 8, 0, 0)
        duracionDescanso = datetime(2024, 6, 13, 0, 5, 0)
        estado = True
        ID_Usuario = 1
        nuevo_pomodoro = self.pomodoro_crud.create_pomodoro(duracionTrabajo, horaInicio, duracionDescanso, estado, ID_Usuario)
        self.session.commit()
        self.pomodoro_crud.delete_pomodoro(nuevo_pomodoro.ID_Pomodoro)
        self.session.commit()
        deleted_pomodoro = self.pomodoro_crud.get_pomodoro_by_id(nuevo_pomodoro.ID_Pomodoro)
        self.assertIsNone(deleted_pomodoro)

if __name__ == '__main__':
    unittest.main()
