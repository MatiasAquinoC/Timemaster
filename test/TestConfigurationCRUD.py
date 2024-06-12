import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.CreateDatabase import Base, Configuracion
from src.logica.ConfiguracionCRUD import configuracion  # Asegúrate de importar la clase CRUD para Configuracion

class TestConfiguracionCRUDOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()
        cls.configuracion_crud = configuracion

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def setUp(self):
        # Reiniciar la base de datos antes de cada prueba
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)

    def test_create_configuracion(self):
        configuracionModo = True
        configuracionReloj = "Digital"
        configuracionFuente = 12
        ID_Usuario = 1
        nueva_configuracion = self.configuracion_crud.create_configuracion(configuracionModo, configuracionReloj, configuracionFuente, ID_Usuario)
        self.assertIsNotNone(nueva_configuracion)
        self.assertEqual(nueva_configuracion.configuracionModo, configuracionModo)
        self.assertEqual(nueva_configuracion.configuracionReloj, configuracionReloj)
        self.assertEqual(nueva_configuracion.configuracionFuente, configuracionFuente)
        self.assertEqual(nueva_configuracion.ID_Usuario, ID_Usuario)

    def test_get_configuracion_by_id(self):
        configuracionModo = True
        configuracionReloj = "Digital"
        configuracionFuente = 12
        ID_Usuario = 1
        nueva_configuracion = self.configuracion_crud.create_configuracion(configuracionModo, configuracionReloj, configuracionFuente, ID_Usuario)
        fetched_configuracion = self.configuracion_crud.get_configuracion_by_id(nueva_configuracion.ID_Configuracion)
        self.assertIsNotNone(fetched_configuracion)
        self.assertEqual(fetched_configuracion.ID_Configuracion, nueva_configuracion.ID_Configuracion)

    def test_update_configuracion(self):
        configuracionModo = True
        configuracionReloj = "Digital"
        configuracionFuente = 12
        ID_Usuario = 1
        nueva_configuracion = self.configuracion_crud.create_configuracion(configuracionModo, configuracionReloj, configuracionFuente, ID_Usuario)
        updated_configuracion = self.configuracion_crud.update_configuracion(nueva_configuracion.ID_Configuracion, configuracionModo=False, configuracionReloj="Analógico")
        self.assertIsNotNone(updated_configuracion)
        self.assertFalse(updated_configuracion.configuracionModo)
        self.assertEqual(updated_configuracion.configuracionReloj, "Analógico")

    def test_delete_configuracion(self):
        configuracionModo = True
        configuracionReloj = "Digital"
        configuracionFuente = 12
        ID_Usuario = 1
        nueva_configuracion = self.configuracion_crud.create_configuracion(configuracionModo, configuracionReloj, configuracionFuente, ID_Usuario)
        self.configuracion_crud.delete_configuracion(nueva_configuracion.ID_Configuracion)
        deleted_configuracion = self.configuracion_crud.get_configuracion_by_id(nueva_configuracion.ID_Configuracion)
        self.assertIsNone(deleted_configuracion)

if __name__ == '__main__':
    unittest.main()
