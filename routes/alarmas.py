from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, jsonify
from models.alarmas import Alarma
from utils.db import db
from flask_login import login_required
from datetime import datetime

alarmas = Blueprint('alarma', __name__)

@alarmas.route('/alarma')
@login_required
def alarma():
    alarmas = Alarma.query.all()
    hora_actual = datetime.now().time() 

    mostrar_modal = False

    for alarma in alarmas:
        if alarma.hora_inicio == hora_actual.strftime('%H:%M'):
            mostrar_modal = True
            break

    csrf_enabled = current_app.config.get('WTF_CSRF_ENABLED', True)
    return render_template('alarma.html', alarmas=alarmas, csrf_enabled=csrf_enabled, mostrar_modal=mostrar_modal)

@alarmas.route('/verificar_alarma')
@login_required
def verificar_alarma():
    alarmas = Alarma.query.all()
    hora_actual = datetime.now().time() 

    mostrar_modal = False
    for alarma in alarmas:
        if alarma.hora_inicio == hora_actual.strftime('%H:%M'):
            mostrar_modal = True
            break

    return jsonify(mostrar_modal=mostrar_modal)

@alarmas.route('/crearAlarma', methods=['POST'])
@login_required
def addContact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        hora_inicio = request.form['hora_inicio']
        

        new_alarm = Alarma(nombre, hora_inicio, 1)

        db.session.add(new_alarm)
        db.session.commit()
        flash('Alarm added successfully!')
        
        return redirect(url_for('alarma.alarma'))


@alarmas.route('/alarma/<id>', methods = ['POST','GET'])
@login_required
def update(id):
    alarma = Alarma.query.get(id)
    if request.method == 'POST':
        alarma.nombre = request.form['nombre']
        alarma.hora_inicio = request.form['hora_inicio']

        if request.form['estado'] == "true":
            alarma.estado = 1
        else:
            alarma.estado = 0

        db.session.commit()
        flash("Alarma updated successfully!!")
        return redirect(url_for('alarma.alarma'))
    csrf_enabled = current_app.config.get('WTF_CSRF_ENABLED', True) 
    mostrar_modal = False
    return render_template('update.html', alarma = alarma,csrf_enabled=csrf_enabled,mostrar_modal=mostrar_modal)

@alarmas.route('/deleteAlarma/<id>')
@login_required
def delete(id):
    alarma = Alarma.query.get(id)
    db.session.delete(alarma)
    db.session.commit()

    flash("Alarma deleted successfully!!")

    return redirect(url_for('alarma.alarma'))
