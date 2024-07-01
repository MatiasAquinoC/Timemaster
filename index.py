from app import app
from utils.db import db
from flask import redirect, url_for
from flask_wtf.csrf import CSRFProtect

def status_401(error):
    return redirect(url_for('usuarios.login'))

def status_404(error):
    return "<h1>No tienes permiso para acceder a esta página <h1>", 404

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    csrf = CSRFProtect()
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(debug=True)
