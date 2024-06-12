import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.CreateDatabase import Base, Alarma
from src.logica.AlarmaCRUD import alarma

class TestAlarmaCRUDOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()
        cls.alarma_crud = alarma

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def setUp(self):
        # Reiniciar la base de datos antes de cada prueba
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)

    def test_create_alarma(self):
        nombre = "Alarma Test"
        horaInicio = datetime(2024, 6, 13, 8, 0, 0)
        estado = True
        sonido = "Beep"
        ID_Usuario = 1
        nueva_alarma = self.alarma_crud.create_alarma(nombre, horaInicio, estado, sonido, ID_Usuario)
        self.assertIsNotNone(nueva_alarma)
        self.assertEqual(nueva_alarma.nombre, nombre)
        self.assertEqual(nueva_alarma.horaInicio, horaInicio)
        self.assertTrue(nueva_alarma.estado)
        self.assertEqual(nueva_alarma.sonido, sonido)
        self.assertEqual(nueva_alarma.ID_Usuario, ID_Usuario)

    def test_get_alarma_by_id(self):
        nombre = "Alarma Test"
        horaInicio = datetime(2024, 6, 13, 8, 0, 0)
        estado = True
        sonido = "Beep"
        ID_Usuario = 1
        nueva_alarma = self.alarma_crud.create_alarma(nombre, horaInicio, estado, sonido, ID_Usuario)
        fetched_alarma = self.alarma_crud.get_alarma_by_id(nueva_alarma.ID_Alarma)
        self.assertIsNotNone(fetched_alarma)
        self.assertEqual(fetched_alarma.ID_Alarma, nueva_alarma.ID_Alarma)

    def test_update_alarma(self):
        nombre = "Alarma Test"
        horaInicio = datetime(2024, 6, 13, 8, 0, 0)
        estado = True
        sonido = "Beep"
        ID_Usuario = 1
        nueva_alarma = self.alarma_crud.create_alarma(nombre, horaInicio, estado, sonido, ID_Usuario)
        updated_alarma = self.alarma_crud.update_alarma(nueva_alarma.ID_Alarma, nombre="Alarma Actualizada", estado=False)
        self.assertIsNotNone(updated_alarma)
        self.assertEqual(updated_alarma.nombre, "Alarma Actualizada")
        self.assertFalse(updated_alarma.estado)

    def test_delete_alarma(self):
        nombre = "Alarma Test"
        horaInicio = datetime(2024, 6, 13, 8, 0, 0)
        estado = True
        sonido = "Beep"
        ID_Usuario = 1
        nueva_alarma = self.alarma_crud.create_alarma(nombre, horaInicio, estado, sonido, ID_Usuario)
        self.alarma_crud.delete_alarma(nueva_alarma.ID_Alarma)
        deleted_alarma = self.alarma_crud.get_alarma_by_id(nueva_alarma.ID_Alarma)
        self.assertIsNone(deleted_alarma)

if __name__ == '__main__':
    unittest.main()