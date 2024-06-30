from flask import Blueprint, render_template, request, redirect, url_for, flash 
from flask_login import login_required

cronometros = Blueprint('cronometro', __name__)

@cronometros.route('/cronometro')
@login_required
def cronometro():
    return render_template('cronometro.html')

