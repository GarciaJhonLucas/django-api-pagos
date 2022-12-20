# Django Portafolio Backend

## Setup

Como obtener este proyecto en su directorio:

```sh
$ git clone https://github.com/GarciaJhonLucas/django-api-rest-pagos.git
$ cd django-api-rest-pagos
```

Crear un entorno virtual y activarlo para posterior instalar las librerias:

```sh
$ python -m virtualenv env

# windows
$ source env/Scripts/activate
# Linux
$ source env/bin/activate
```

Luego instalar las librerias:

```sh
(env) $ pip install -r libs.txt
```

Observe el `(env)` delante de la linea de su terminal. Esto indica que esta sesión de terminal opera en un `entorno virtual` configurado por `virtualenv`.

Una vez que `pip` haya terminado de descargar las dependencias:

Luego ejecutamos las migraciones para crear la base de datos de nuesta aplicacion, todo dentro de nuestro entorno virtual.

```sh
# De manera general
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate

# Para nuestro proyecto
```

Una vez concluido, procedemos a iniciar la app
```sh
(env) $ python manage.py runserver
```

## Hacer uso del proyecto

Navegue hasta `http://127.0.0.1:8000/`

Ahora para hacer uso del proyecto, crear un proyecto navege hacia `http://127.0.0.1:8000/login`.

Selecionas que no tienes cuenta para luego ir a `http://127.0.0.1:8000/register/` 

Crear un usuario con los datos que te pide, luego te redirige al login

Ingresas tus datos recien creados, te llevara a `http://127.0.0.1:8000/create/` 

Rellenas los datos y listo ya se crea un proyecto, el cual podras ver en `http://127.0.0.1:8000/` ****