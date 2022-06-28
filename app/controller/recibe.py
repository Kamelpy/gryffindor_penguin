from flask import Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import config
from models import db, Residente_envia, Residente_recibe, Involucrado
import requests
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/form_receptor')
def form_receptor():
    return render_template("form_receptor.html")

@bp.route("/api/v1", methods =['POST'])
def apiv1():
    datos_receptor=request.form
    print(datos_receptor)
    fecha_actual=datetime.now()
    residente_recibe=Residente_recibe.create(
    nombre=datos_receptor["nombre"], 
    apellido=datos_receptor["apellido"], 
    cedula_identidad=datos_receptor["cedula_identidad"],
    edad=datos_receptor["edad"],
    telefono=datos_receptor["telefono"], 
    latitud=datos_receptor["latitud"], 
    longitud=datos_receptor["longitud"], 
    fecha_registro=fecha_actual)

    return render_template("form_receptor.html")
