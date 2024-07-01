import pytest
from flask import url_for
from models.alarmas import Alarma
from utils.db import db
import traceback

@pytest.mark.usefixtures('client', 'auth_client')
def test_add_alarma(auth_client, client, db):
    try:
        auth_client()

        response = client.post('/crearAlarma', data={
            'nombre': 'Test Alarma',
            'hora_inicio': '12:00',
        }, follow_redirects=True)
        assert response.status_code == 200

        alarma = Alarma.query.filter_by(nombre='Test Alarma').first()
        assert alarma is not None
        assert alarma.hora_inicio == '12:00'
    except Exception as e:
        print(f"Error in test_add_alarma: {e}")
        print(traceback.format_exc())
        raise e

@pytest.mark.usefixtures('client', 'auth_client')
def test_update_alarma(auth_client, client, db):
    try:
        auth_client()  # Iniciar sesión antes de hacer la solicitud
        alarma = Alarma(nombre='Alarma a Actualizar', hora_inicio='15:00', estado=True)
        db.session.add(alarma)
        db.session.commit()

        response = client.post(url_for('alarma.update', id=alarma.id_alarma), data={
            'nombre': 'Updated Alarma',
            'hora_inicio': '16:00',
            'estado': 'false',
        }, follow_redirects=True)
        assert response.status_code == 200

        updated_alarma = Alarma.query.filter_by(id_alarma=alarma.id_alarma).first()
        assert updated_alarma.nombre == 'Updated Alarma'
        assert updated_alarma.hora_inicio == '16:00'
        assert not updated_alarma.estado
    except Exception as e:
        print(f"Error in test_add_alarma: {e}")
        print(traceback.format_exc())
        raise e

@pytest.mark.usefixtures('client', 'auth_client')
def test_delete_alarma(auth_client, client, db):
    try:
        auth_client() 
        alarma = Alarma(nombre='Alarma a Eliminar', hora_inicio='18:00', estado=True)
        db.session.add(alarma)
        db.session.commit()

        response = client.get(url_for('alarma.delete', id=alarma.id_alarma), data={
        }, follow_redirects=True)
        assert response.status_code == 200

        deleted_alarma = Alarma.query.filter_by(id_alarma=alarma.id_alarma).first()
        assert deleted_alarma is None
    except Exception as e:
        print(f"Error in test_add_alarma: {e}")
        print(traceback.format_exc())
        raise e