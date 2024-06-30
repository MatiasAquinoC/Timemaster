from flask import Blueprint, render_template, request, redirect, url_for, flash 
from models.alarmas import Alarma
from utils.db import db
from flask_login import login_required

alarmas = Blueprint('alarma', __name__)

@alarmas.route('/alarma')
@login_required
def alarma():
    alarmas = Alarma.query.all()
    return render_template('alarma.html', alarmas = alarmas)

@alarmas.route('/crearAlarma', methods=['POST'])
@login_required
def addContact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        hora = request.form['hora']
        new_alarm = Alarma(nombre, hora, 1)

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
    
    return render_template('update.html', alarma = alarma)

@alarmas.route('/deleteAlarma/<id>')
@login_required
def delete(id):
    alarma = Alarma.query.get(id)
    db.session.delete(alarma)
    db.session.commit()

    flash("Alarma deleted successfully!!")

    return redirect(url_for('alarma.alarma'))
