from flask import (
    Blueprint, render_template,request
)
import datetime
from config import config
from models import db, Involucrado

bp = Blueprint('main', __name__)


@bp.route('/form_involved')
def form_involved():
    #Renderizamos la plantilla. Formulario HTML
    # templates/form.html
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