from flask import ( 
    Blueprint, render_template, request
)
from datetime import datetime
from app.model import Residente_envia, Residente_recibe
bp = Blueprint('envia', __name__)
from haversine import haversine, Unit


@bp.route('/alertar')
def alertar():
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
    punto_a_comparar=(float(datos_informer["latitud"]),float(datos_informer["longitud"]))
    print(punto_a_comparar)    
    lista_coordenadas_recibe=Residente_recibe.query.all()
    print(lista_coordenadas_recibe)
    extracion_coordenadas_recibe=[]
    for elemento in lista_coordenadas_recibe:
        coordenadas_especificas_residente_recibe_lat_lon=[elemento.latitud , elemento.longitud]  
        extracion_coordenadas_recibe.append(coordenadas_especificas_residente_recibe_lat_lon) 
    print(extracion_coordenadas_recibe) 
    
    for point in extracion_coordenadas_recibe:
        marcador_recibe = (point[0] , point[1])
        distancia=haversine(punto_a_comparar, marcador_recibe)
        print(distancia)
    return render_template("form_informer.html")

