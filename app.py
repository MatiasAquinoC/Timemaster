from flask import  Flask
from routes.pomodoro import pomodoro
from routes.usuarios import usuarios
from routes.alarmas import alarmas
from routes.cronometro import cronometros
from routes.temporizador import temporizadores
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from flask_login import LoginManager
from models.usuarios import Usuario

app = Flask(__name__)

app.secret_key = "secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jAZCoqCuPCosufYyDcuSIKCHWAjfFXNi@roundhouse.proxy.rlwy.net:45746/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager_app = LoginManager(app)
@login_manager_app.user_loader
def load_user(id):
    return Usuario.query.filter_by(id_usuario=id).first()

app.register_blueprint(pomodoro)
app.register_blueprint(usuarios)
app.register_blueprint(alarmas)
app.register_blueprint(cronometros)
app.register_blueprint(temporizadores)
