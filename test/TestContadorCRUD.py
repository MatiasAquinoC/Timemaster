import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.CreateDatabase import Base, Contador
from src.logica.ContadorCRUD import contador  # Asegúrate de importar la clase CRUD para Contador
from datetime import datetime
class TestContadorCRUDOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()
        cls.contador_crud = contador

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def setUp(self):
        # Reiniciar la base de datos antes de cada prueba
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)

    def test_create_contador(self):
        nombre = "Contador Test"
        fechaInicio = datetime(2024, 6, 13, 8, 0, 0)
        fechaFin = datetime(2024, 6, 13, 8, 30, 0)
        ID_Usuario = 1
        nuevo_contador = self.contador_crud.create_contador(nombre, fechaInicio, fechaFin, ID_Usuario)
        self.assertIsNotNone(nuevo_contador)
        self.assertEqual(nuevo_contador.nombre, nombre)
        self.assertEqual(nuevo_contador.fechaInicio, fechaInicio)
        self.assertEqual(nuevo_contador.fechaFin, fechaFin)
        self.assertEqual(nuevo_contador.ID_Usuario, ID_Usuario)

    def test_get_contador_by_id(self):
        nombre = "Contador Test"
        fechaInicio = datetime(2024, 6, 13, 8, 0, 0)
        fechaFin = datetime(2024, 6, 13, 8, 30, 0)
        ID_Usuario = 1
        nuevo_contador = self.contador_crud.create_contador(nombre, fechaInicio, fechaFin, ID_Usuario)
        fetched_contador = self.contador_crud.get_contador_by_id(nuevo_contador.ID_Conteo)
        self.assertIsNotNone(fetched_contador)
        self.assertEqual(fetched_contador.ID_Conteo, nuevo_contador.ID_Conteo)

    def test_update_contador(self):
        nombre = "Contador Test"
        fechaInicio = datetime(2024, 6, 13, 8, 0, 0)
        fechaFin = datetime(2024, 6, 13, 8, 30, 0)
        ID_Usuario = 1
        nuevo_contador = self.contador_crud.create_contador(nombre, fechaInicio, fechaFin, ID_Usuario)
        updated_contador = self.contador_crud.update_contador(nuevo_contador.ID_Conteo, nombre="Nuevo Nombre", fechaInicio=datetime(2024, 6, 13, 9, 0, 0))
        self.assertIsNotNone(updated_contador)
        self.assertEqual(updated_contador.nombre, "Nuevo Nombre")
        self.assertEqual(updated_contador.fechaInicio, datetime(2024, 6, 13, 9, 0, 0))

    def test_delete_contador(self):
        nombre = "Contador Test"
        fechaInicio = datetime(2024, 6, 13, 8, 0, 0)
        fechaFin = datetime(2024, 6, 13, 8, 30, 0)
        ID_Usuario = 1
        nuevo_contador = self.contador_crud.create_contador(nombre, fechaInicio, fechaFin, ID_Usuario)
        self.contador_crud.delete_contador(nuevo_contador.ID_Conteo)
        deleted_contador = self.contador_crud.get_contador_by_id(nuevo_contador.ID_Conteo)
        self.assertIsNone(deleted_contador)

if __name__ == '__main__':
    unittest.main()
