import unittest
from src.modelo.createDatabase import Base, create_engine, sessionmaker
from src.logica.usuarioCRUD import usuarioCRUD

class TestUsuarioCRUD(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Asegura que la sesión esté disponible para todas las pruebas
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
    def setUp(self):
        # Limpia la tabla de Usuario antes de cada prueba
        self.session = self.Session()
        self.usuario_crud = usuarioCRUD(self.session)
    def tearDown(self):
        self.session.close()
    def test_create_usuario(self):
        usuario_creado = self.usuario_crud.create_usuario("Juan Pérez", "juan@example.com", "password123")
        print(usuario_creado)
        self.assertIsNotNone(usuario_creado.ID_Usuario)
        self.assertEqual(usuario_creado.nombre, "Juan Pérez")
        self.assertEqual(usuario_creado.contraseña, "password123")

    def test_get_usuario_by_id(self):
        usuario_creado = self.usuario_crud.create_usuario("Ana López", "ana@example.com", "abcde")
        self.assertIsNotNone(usuario_creado)
        usuario_obtenido = self.usuario_crud.get_usuario_by_id(usuario_creado.ID_Usuario)
        self.assertIsNotNone(usuario_obtenido)
        self.assertEqual(usuario_obtenido.nombre, "Ana López")
        self.assertEqual(usuario_obtenido.email, "ana@example.com")

    def test_update_usuario(self):
        usuario_creado = self.usuario_crud.create_usuario("Pedro Gómez", "pedro@example.com", "oldpassword")
        self.assertIsNotNone(usuario_creado)
        usuario_actualizado = self.usuario_crud.update_usuario(usuario_creado.ID_Usuario, nombre="Pedro Pérez", contraseña="newpassword")
        self.assertIsNotNone(usuario_actualizado)
        self.assertEqual(usuario_actualizado.nombre, "Pedro Pérez")
        self.assertEqual(usuario_actualizado.contraseña, "newpassword")

    def test_delete_usuario(self):
        usuario_creado = self.usuario_crud.create_usuario("María Martínez", "maria@example.com", "securepassword")
        self.assertIsNotNone(usuario_creado)
        usuario_eliminado = self.usuario_crud.delete_usuario(usuario_creado.ID_Usuario)
        self.assertIsNone(usuario_eliminado)


if __name__ == '__main__':
    unittest.main()
