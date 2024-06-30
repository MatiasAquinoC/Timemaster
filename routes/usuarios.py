from flask import Blueprint, render_template, request, redirect, url_for, flash 
from models.usuarios import Usuario
from utils.db import db
from flask_login import LoginManager, login_user, logout_user

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/')
def index():
    return redirect(url_for('usuarios.login'))


@usuarios.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        usuario = Usuario.query.filter_by(nombre=username).first()
        
        if(usuario != None):
            login_user(usuario)
            return redirect(url_for('alarma.alarma'))
        
        flash("Usuario not found!")
        return render_template('login.html')
    else:
        return render_template('login.html')
    
@usuarios.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('usuarios.login'))
    
@usuarios.route('/crearUsuario', methods=['POST'])
def addContact():
    nombre = request.form['nombre']
    email = request.form['email']
    contrasena = request.form['contrasena']
    
    new_usuario = Usuario(nombre, email, contrasena)
    db.session.add(new_usuario)
    db.session.commit()

    flash("Usuario added successfully!")
    return redirect(url_for('contacts.index'))

@usuarios.route('/usuarios/<id>', methods = ['POST','GET'])
def update(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.email = request.form['email']
        usuario.contrasena = request.form['contrasena']

        db.session.commit()
        flash("Usuario updated successfully!!")
        return redirect(url_for('contacts.index'))
    
    return render_template('update.html', usuario = usuario)

@usuarios.route('/deleteUsuario/<id>')
def delete(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()

    flash("Usuario deleted successfully!!")

    return redirect(url_for('contacts.index'))
