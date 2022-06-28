from flask import (
    Blueprint, render_template
)
from flask import request
import datetime
from config import config
from models import db, Residente_envia
bp = Blueprint('main', __name__)


@bp.route('/form_receptor')
def form_receptor():
    #Renderizamos la plantilla. Formulario HTML
    # templates/form.html
    return render_template("form_receptor.html")
    

@bp.route('/api/v2',methods=['POST'])
def apiv2():
    datos_informer=request.form
    print(datos_informer)
    fecha_actual=datetime.now()
    residente_envia=Residente_envia.create(
    nombre=datos_informer["nombre"], 
    apellido=datos_informer["apellido"], 
    cedula_identidad=datos_informer["cedula_identidad"],
    edad=datos_informer["edad"],
    telefono=datos_informer["telefono"], 
    latitud=datos_informer["latitud"], 
    longitud=datos_informer["longitud"], 
    fecha_registro=fecha_actual
    )
    return render_template("form_informer.html")