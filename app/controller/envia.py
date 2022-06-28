from flask import ( 
    Blueprint, render_template, request
)
import datetime
from app.model import Residente_envia
bp = Blueprint('envia', __name__)


@bp.route('/form_informer')
def form_informer():
    #Renderizamos la plantilla. Formulario HTML
    # templates/form.html
    return render_template("form_informer.html")
    

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