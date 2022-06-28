from flask import (
    Blueprint, render_template,request
)
from datetime import datetime
from app.model import Involucrado

bp = Blueprint('involucrado', __name__)


@bp.route('/involucrate')
def involucrate():
    return render_template("form_involved.html")

@bp.route('/api/v3',methods=['POST'])
def apiv3():
    datos_involved=request.form
    print(datos_involved)
    fecha_actual=datetime.now()
    involucrado=Involucrado.create(
    nombre=datos_involved["nombre"], 
    apellido=datos_involved["apellido"], 
    cedula_identidad=datos_involved["cedula_identidad"],
    telefono=datos_involved["telefono"], 
    servicio_a_ofrecer=datos_involved["servicio_a_ofrecer"],
    fecha_registro=fecha_actual
    )
    return render_template("form_involved.html")