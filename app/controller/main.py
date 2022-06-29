from flask import (
    Blueprint, render_template
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index2.html')

@bp.route('/soluciones')
def soluciones():
    return render_template('soluciones2.html')
    
@bp.route('/mas-info')
def mas_info():
    return render_template('mas-info.html')

@bp.route('/donaciones')
def donaciones():
    return render_template("donaciones2.html")

@bp.route('/problematica')
def problematica():
    return render_template("problematica.html")

@bp.route('/que-hacer')
def que_hacer():
    return render_template("que-hacer.html")

@bp.route('/conocenos')
def conocenos():
    return render_template("conocenos.html")

