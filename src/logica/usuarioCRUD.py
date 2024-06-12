from src.modelo.createDatabase import Usuario  # Asegúrate de importar el modelo y la base de datos

class usuarioCRUD:
    def __init__(self, session):
        self.session = session
    def create_usuario(self, nombre, email, contraseña):
        nuevo_usuario = Usuario(nombre=nombre, email=email, contraseña=contraseña)
        self.session.add(nuevo_usuario)
        self.session.commit()
        return nuevo_usuario

    def get_usuario_by_id(self, usuario_id):
        return self.session.query(Usuario).filter(Usuario.ID_Usuario == usuario_id).first()

    def update_usuario(self, usuario_id, nombre=None, email=None, contraseña=None):
        usuario = self.session.query(Usuario).filter(Usuario.ID_Usuario == usuario_id).first()
        if usuario:
            if nombre:
                usuario.nombre = nombre
            if email:
                usuario.email = email
            if contraseña:
                usuario.contraseña = contraseña
            self.session.commit()
        return usuario
    def delete_usuario(self,usuario_id):
        usuario = self.session.query(Usuario).filter(Usuario.ID_Usuario == usuario_id).first()
        if usuario:
            self.session.delete(usuario)
            self.session.commit()
            return None
        return usuario