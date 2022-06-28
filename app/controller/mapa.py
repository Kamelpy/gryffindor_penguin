from flask import Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy
from app.model import Residente_recibe, Residente_envia, Involucrado
import requests
from datetime import datetime
import folium
from folium.plugins import MarkerCluster
from haversine import haversine, Unit

bp = Blueprint('mapa', __name__)


@bp.route('/mapa')

def mapa():
    mapa=folium.Map(location=[-25.3011646,-57.6320055],width="50%",height="50%",zoom_start=13)
    cluster=MarkerCluster().add_to(mapa)
    
    ##Resindentes que quieren recibir alertas
    lista_coordenadas_recibe=Residente_recibe.query.all()
    print(lista_coordenadas_recibe)
    extracion_coordenadas_recibe=[]
    for elemento in lista_coordenadas_recibe:
        coordenadas_especificas_residente_recibe_lat_lon=[elemento.latitud , elemento.longitud]  
        extracion_coordenadas_recibe.append(coordenadas_especificas_residente_recibe_lat_lon) 
    print(extracion_coordenadas_recibe) 
    for point in extracion_coordenadas_recibe:
        marcador_recibe = point[0] , point[1]
        folium.Marker(location=marcador_recibe , icon=folium.Icon(color="green")).add_to(cluster)

    ##Resindentes que quieren envien alertas
    lista_coordenadas_envia=Residente_envia.query.all()
    print(lista_coordenadas_envia)
    extracion_coordenadas_envia=[]
    for elemento in lista_coordenadas_envia:
        coordenadas_especificas_residente_envia_lat_lon=[elemento.latitud , elemento.longitud]  
        extracion_coordenadas_envia.append(coordenadas_especificas_residente_envia_lat_lon) 
    print(extracion_coordenadas_envia) 
    for point in extracion_coordenadas_envia:
        marcador_envia = point[0] , point[1]
        folium.Marker(location=marcador_envia,  icon=folium.Icon(color="blue")).add_to(cluster)


    return mapa._repr_html_()
