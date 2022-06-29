from flask import (
    Blueprint, render_template
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index2.html')

@bp.route('/soluciones')
def soluciones():
    return render_template('soluciones.html')

@bp.route('/donaciones')
def donaciones():
    return render_template("donaciones.html")

