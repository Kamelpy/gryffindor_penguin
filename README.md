# PLATAFORMA S.A.I WEB
### (Sistema de Alerta ante Inundaciones)


_S.A.I, es una aplicación creada con la idea de comunicar a personas afectadas por inundaciones en sus viviendas y, de esa manera puedan alertarse y ayudarse mutuamente.
¿Para qué creamos SIAP? Durante las inundaciones, las personas sufren de un problema común: la incapacidad de comunicarse efectivamente entre sí al momento que el agua invade sus viviendas.
Y la total ausencia de un sistema de contingencia y ayuda cuando hay una inundación. S.A.I da la oportunidad al usuario de ser notificado por otro usuario cuando el agua crece, y a partir de esa información solicitar ayuda o ayudar a quienes los necesiten.
**Está pensada para optimizar el sentido de solidaridad y soporte entre las comunidades que sufren estas condiciones.**_

### Pre-requisitos 📋

_Desde la terminal ubicado en la carpeta raiz del proyecto crear el entorno virtual_
```
#windows
py -m venv venv
```
_Una vez creado procedemos a activar el entorno virtual_
```
#windows
. venv/Scripts/activate
```

_Instalamos los paquetes de requerimientos y ya tendremos todas las librerias necesarias._
```
#windows
pip freeze > requirements.txt
```



## ¿Cómo usar

_Luego de instalar los requerimientos, deberas correr `flask`_
```
Flask run
```

_SI quieres puedes habilitar antes el modo de desarrollo `Debug mode: ON`_
```
export FLASK_ENV=development
```


## Screenshots :iphone:

<p float="left">
<img src="/sai-1.webp"  />
<br></p>

<p float="left">
<img src="/sai-2.webp"  />
<br></p>

<p float="left">
<img src="/sai-3.webp"  />
<br></p>


## Tecnologías usadas :sunglasses:

- [Flask](https://pypi.org/project/Flask/) Python Framework: Ruteo de URLs y Mapeo HTML
- [HTML & CSS](https://www.w3schools.com/html/html_css.asp): Estructura y Diseño de Páginas para formulario
- [SqlAlchemy](https://pypi.org/project/SQLAlchemy/) Base de Datos: Para Alojamiento de Datos
- [Folium](https://pypi.org/project/folium/) (Libreria): Para mostrar los datos en un mapa
- [Firebase](https://pypi.org/project/firebase-admin/) (from Google): Para notificaciones push
- [Haversine](https://pypi.org/project/haversine/) (Libreria): Para calculo de distancias

## Integrantes

- [Silvia Canale](https://github.com/SilviCanale)
- Eduardo Cañete
- Cesar Franco
- [Nicolas Portillo](https://github.com/Kamelpy)
- [José Arzamendia](https://github.com/josemarza)


## Coach

- [Steven Britez](https://github.com/reybritez)

## Mentor

- [Mario Karajallo](https://github.com/mariokarajallo)

## Aportes :muscle:

Si quieres aportar, haz un fork de la repo, luego abre tu rama, una vez que hiciste todo lo que quieres agregar, haz un pull request! 😄

## Licencia

El contenido está licenciado bajo MIT License.
