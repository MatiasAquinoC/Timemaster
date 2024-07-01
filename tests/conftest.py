import sys
import os
import pytest
from flask_wtf.csrf import CSRFProtect, generate_csrf

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app as flask_app
from utils.db import db as _db
from models.usuarios import Usuario


@pytest.fixture(scope='module')
def appTest():
    flask_app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False, 
        "SQLALCHEMY_DATABASE_URI": 'sqlite:///:memory:',
        "SQLALCHEMY_TRACK_MODIFICATIONS": False, 
        "SERVER_NAME": "localhost" 
    })

    with flask_app.app_context():
        _db.create_all() 
        yield flask_app
        _db.drop_all()

@pytest.fixture(scope='module')
def db(appTest):
    with appTest.app_context():
        _db.create_all()
        yield _db
        _db.session.remove()
        _db.drop_all()

@pytest.fixture(scope='module')
def client(appTest):
    return appTest.test_client()

@pytest.fixture(scope='module')
def auth_client(client, appTest):
    def login():
        with appTest.app_context():
            user = Usuario(nombre='testuser', email='test@example.com', contrasena='password')
            _db.session.add(user)
            _db.session.commit()

            response = client.post('/login', data={
                'username': 'testuser',
                'password': 'password',
            }, follow_redirects=True)
            assert response.status_code == 200

        return client

    return login