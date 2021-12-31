# django-iban-app
## Simple CRUD application built in Django with Google OAuth and Django admin module

The project was built on Windows machine. Python 3.10. Only used main branch. In common scenario, use branch per environment

Steps followed for development:

**Download and install main tools**
- Git
- Python
- VSCode
- PostgreSQL for Windows

**For testing**
- Docker Desktop (for Windows)

**Create virtual env and install all python packages (check requirements.txt)**
- Django
- psycopg2
- django-allauth
- django-localflavor

**Set up and activate venv**
python -m venv iban-app-env

iban-app-env is not in repo, instead, you can find all dependencies in requirement.txt file

django-admin startproject iban_app -> To create new project

**PostgreSQL setup**
- Install PostgreSQL for windows and configure (default login: postgres/postgres)
- pip install psycopg2

**Setup database in settings.py**
python manage.py makemigrations 
python manage.py migrate
python manage.py createsuperuser 

**OAuth setup**
pip install django-allauth
Configure settings.py
Add Site to django admin -> 127.0.0.1:8000

SITE_ID to 3 in settings.py
**IMPORTAN!** This value is de id from Site object. It should match with the one we already created
If you face this error while login:

![SITE_ID error](https://github.com/Habbi95/django-iban-app/blob/766e43f26131665d3ea5b967a963327e8723f8b7/screenshots/image.png)

Please check this SITE_ID value in settings.py and modify it with other one
    
**Setup Google API Gmail OAuth account**
- OAuth consent screen
- Create credentials
- Set up javascript origin and redirect URI


**Create Social app in django admin**
- Add keys and id

**IBAN validation (models and form)**
pip install django-localflavor

### LAUNCH docker_compose environment

I made a Dockerfile with the django image. It will copy all the django project into the container.
The docker_compose.yml will create two containers: a postgres one based on existing image and the django we already built

It will launch some basic testing to the models and views, then prepare the configuration and run the server.

To kick off this, just clone this repo, and in the same directory run: **docker_compose up**

Download the video:
(https://github.com/Habbi95/django-iban-app/blob/99ba03ff04302e1d768cfc633d9e2369f7b722ed/screenshots/screen-capture.webm)
