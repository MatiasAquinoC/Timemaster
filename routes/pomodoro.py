from flask import Blueprint, render_template, request, redirect, url_for, flash 
from models.pomodoro import Pomodoro
from utils.db import db
from flask_login import login_required

pomodoro = Blueprint('pomodoro', __name__)

@pomodoro.route('/pomodoro')
@login_required
def index():    
    pomodoro = Pomodoro.query.all()
    return render_template('pomodoro.html', pomodoro = pomodoro)

@pomodoro.route('/newPomodoro', methods=['POST'])
@login_required
def addContact():
    duracion_trabajo = request.form['duracion_trabajo']
    duracion_descanso = request.form['duracion_descanso']
    
    new_pomodoro = Pomodoro(duracion_trabajo, duracion_descanso)
    db.session.add(new_pomodoro)
    db.session.commit()

    flash("Pomodoro added successfully!")
    return redirect(url_for('contacts.index'))

@pomodoro.route('/pomodoro/<id>', methods = ['POST','GET'])
@login_required
def update(id):
    pomodoro = Pomodoro.query.get(id)
    if request.method == 'POST':
        pomodoro.duracion_trabajo = request.form['duracion_trabajo']
        pomodoro.duracion_descanso = request.form['duracion_descanso']

        db.session.commit()
        flash("Pomodoro updated successfully!!")
        return redirect(url_for('contacts.index'))
    
    return render_template('update.html', contact = pomodoro)

@pomodoro.route('/deletePomodoro/<id>')
@login_required
def delete(id):
    pomodoro = Pomodoro.query.get(id)
    db.session.delete(pomodoro)
    db.session.commit()

    flash("Pomodoro deleted successfully!!")

    return redirect(url_for('contacts.index'))
