import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.CreateDatabase import Base, Cronometro
from src.logica.CronometroCRUD import cronometro  # Asegúrate de importar la clase CRUD para Cronometro

class TestCronometroCRUDOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()
        cls.cronometro_crud = cronometro

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def setUp(self):
        # Reiniciar la base de datos antes de cada prueba
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)

    def test_create_cronometro(self):
        fechaInicio = datetime(2024, 6, 13, 8, 0, 0)
        duracion = datetime(2024, 6, 13, 8, 30, 0)
        fechasParciales = datetime(2024, 6, 13, 8, 15, 0)
        ID_Usuario = 1
        nuevo_cronometro = self.cronometro_crud.create_cronometro(fechaInicio, duracion, fechasParciales, ID_Usuario)
        self.assertIsNotNone(nuevo_cronometro)
        self.assertEqual(nuevo_cronometro.fechaInicio, fechaInicio)
        self.assertEqual(nuevo_cronometro.duracion, duracion)
        self.assertEqual(nuevo_cronometro.fechasParciales, fechasParciales)
        self.assertEqual(nuevo_cronometro.ID_Usuario, ID_Usuario)

    def test_get_cronometro_by_id(self):
        fechaInicio = datetime(2024, 6, 13, 8, 0, 0)
        duracion = datetime(2024, 6, 13, 8, 30, 0)
        fechasParciales = datetime(2024, 6, 13, 8, 15, 0)
        ID_Usuario = 1
        nuevo_cronometro = self.cronometro_crud.create_cronometro(fechaInicio, duracion, fechasParciales, ID_Usuario)
        fetched_cronometro = self.cronometro_crud.get_cronometro_by_id(nuevo_cronometro.ID_Cronometro)
        self.assertIsNotNone(fetched_cronometro)
        self.assertEqual(fetched_cronometro.ID_Cronometro, nuevo_cronometro.ID_Cronometro)

    def test_update_cronometro(self):
        fechaInicio = datetime(2024, 6, 13, 8, 0, 0)
        duracion = datetime(2024, 6, 13, 8, 30, 0)
        fechasParciales = datetime(2024, 6, 13, 8, 15, 0)
        ID_Usuario = 1
        nuevo_cronometro = self.cronometro_crud.create_cronometro(fechaInicio, duracion, fechasParciales, ID_Usuario)
        updated_cronometro = self.cronometro_crud.update_cronometro(nuevo_cronometro.ID_Cronometro, fechaInicio=datetime(2024, 6, 13, 9, 0, 0))
        self.assertIsNotNone(updated_cronometro)
        self.assertEqual(updated_cronometro.fechaInicio, datetime(2024, 6, 13, 9, 0, 0))

    def test_delete_cronometro(self):
        fechaInicio = datetime(2024, 6, 13, 8, 0, 0)
        duracion = datetime(2024, 6, 13, 8, 30, 0)
        fechasParciales = datetime(2024, 6, 13, 8, 15, 0)
        ID_Usuario = 1
        nuevo_cronometro = self.cronometro_crud.create_cronometro(fechaInicio, duracion, fechasParciales, ID_Usuario)
        self.cronometro_crud.delete_cronometro(nuevo_cronometro.ID_Cronometro)
        deleted_cronometro = self.cronometro_crud.get_cronometro_by_id(nuevo_cronometro.ID_Cronometro)
        self.assertIsNone(deleted_cronometro)

if __name__ == '__main__':
    unittest.main()
