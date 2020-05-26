# LDV

Code used during the courses for the Leonard De Vinci school
https://docs.djangoproject.com/en/3.0/

## Commands list

### Installation

* https://www.python.org/downloads/
* pip3 install virtualenv
* virtualenv <nom du dossier vers l'environement> --python=python3
* Set-ExecutionPolicy RemoteSigned (Pour windows seulement | En admin)
* ./<nom du dossier vers l'environement>/Scripts/activate | ./<nom du dossier vers l'environement>/bin/activate
* pip install django
* django-admin startproject <nom du projet>
* python manage.py startapp <nom de l'application>


### Update database

* python manage.py makemigrations
* python manage.py migrate

### Create administrator

* python manage.py createsuperuser


### Start server

* python manage.py runserver


### Run tests

* python manage.py test


## Arborescence

DOSSIER_PRINCIPALE
- dossier_project
  - dossier_configurations_du_projet
  - dossier_application_1
