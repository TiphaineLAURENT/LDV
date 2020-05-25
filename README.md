# LDV
Code used during the courses for the Leonard De Vinci school

## Commands list

### Installation

* https://www.python.org/downloads/
* pip3 install virtualenv
* virtualenv <nom du dossier vers l'environement> --python=python3
* Set-ExecutionPolicy RemoteSigned (En admin)
* ./<nom du dossier vers l'environement>/Scripts/activate | ./<nom du dossier vers l'environement>/bin/activate
* pip install django
* django-admin startproject <nom du projet>


### Update database

* python manage.py makemigrations
* python manage.py migrate

### Create administrator

* python manage.py createsuperuser


### Start server

* python manage.py runserver
