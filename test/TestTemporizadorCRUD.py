import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.CreateDatabase import Base, Temporizador  # Asegúrate de importar el modelo y la base de datos
from src.logica.TemporizadorCRUD import temporizador  # Asegúrate de importar la clase CRUD para Temporizador

class TestTemporizadorCRUDOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.temporizador_crud = temporizador

    def setUp(self):
        self.session = self.Session()
        self.temporizador_crud.session = self.session
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_create_temporizador(self):
        FechaInicio = datetime(2024, 6, 13, 8, 0, 0)
        duracion = datetime(2024, 6, 13, 0, 30, 0)
        sonido = "Beep"
        ID_Usuario = 1
        nuevo_temporizador = self.temporizador_crud.create_temporizador(FechaInicio, duracion, sonido, ID_Usuario)
        self.session.commit()
        self.assertIsNotNone(nuevo_temporizador)
        self.assertEqual(nuevo_temporizador.FechaInicio, FechaInicio)
        self.assertEqual(nuevo_temporizador.duracion, duracion)
        self.assertEqual(nuevo_temporizador.sonido, sonido)
        self.assertEqual(nuevo_temporizador.ID_Usuario, ID_Usuario)

    def test_get_temporizador_by_id(self):
        FechaInicio = datetime(2024, 6, 13, 8, 0, 0)
        duracion = datetime(2024, 6, 13, 0, 30, 0)
        sonido = "Beep"
        ID_Usuario = 1
        nuevo_temporizador = self.temporizador_crud.create_temporizador(FechaInicio, duracion, sonido, ID_Usuario)
        self.session.commit()
        fetched_temporizador = self.temporizador_crud.get_temporizador_by_id(nuevo_temporizador.ID_Temporizador)
        self.assertIsNotNone(fetched_temporizador)
        self.assertEqual(fetched_temporizador.ID_Temporizador, nuevo_temporizador.ID_Temporizador)

    def test_update_temporizador(self):
        FechaInicio = datetime(2024, 6, 13, 8, 0, 0)
        duracion = datetime(2024, 6, 13, 0, 30, 0)
        sonido = "Beep"
        ID_Usuario = 1
        nuevo_temporizador = self.temporizador_crud.create_temporizador(FechaInicio, duracion, sonido, ID_Usuario)
        self.session.commit()
        updated_temporizador = self.temporizador_crud.update_temporizador(nuevo_temporizador.ID_Temporizador, sonido="Alarm", ID_Usuario=2)
        self.session.commit()
        self.assertIsNotNone(updated_temporizador)
        self.assertEqual(updated_temporizador.sonido, "Alarm")
        self.assertEqual(updated_temporizador.ID_Usuario, 2)

    def test_delete_temporizador(self):
        FechaInicio = datetime(2024, 6, 13, 8, 0, 0)
        duracion = datetime(2024, 6, 13, 0, 30, 0)
        sonido = "Beep"
        ID_Usuario = 1
        nuevo_temporizador = self.temporizador_crud.create_temporizador(FechaInicio, duracion, sonido, ID_Usuario)
        self.session.commit()
        self.temporizador_crud.delete_temporizador(nuevo_temporizador.ID_Temporizador)
        self.session.commit()
        deleted_temporizador = self.temporizador_crud.get_temporizador_by_id(nuevo_temporizador.ID_Temporizador)
        self.assertIsNone(deleted_temporizador)

if __name__ == '__main__':
    unittest.main()
