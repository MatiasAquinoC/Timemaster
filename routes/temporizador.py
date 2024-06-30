from flask import Blueprint, render_template, request, redirect, url_for, flash 
from flask_login import login_required

temporizadores = Blueprint('temporizador', __name__)

@temporizadores.route('/temporizador')
@login_required
def temporizador():
    return render_template('temporizador.html')

