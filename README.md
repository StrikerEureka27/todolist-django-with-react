
# Setup project

This guide explain how to setup a django project from scratch. 
This project is a basic django application + restframework implementation example.  

First, we have to establish a virtual enviroment to isolate our project under specific bunch of packages. 

## Virtual enviroment

Create virtual enviroment

```
virtualenv venv
```

Activate environment

```
source venv/bin/activate
```
## Django installation

Install Django pip dependency

```
python -m pip install django
```

Create a new django project

```
django-admin startproject <name> .
```

> . (dot if we want to create to project in the same folder that the environment folder)

Starting a django server 

```
python manage.py runserver
```

Then to create a new app we can use

```
python manage.py startapp <name>
```

To add the app to the main project we have to add app name to INSTALLED_APP list on <project_name>/settings.py

```
INSTALLED_APPS = [
    ...
    '<project_name>'
]
```

Then to migrate the already included apps we execute 

```
python manage.py migrate
```

## Setup REST FRAMEWORK

Installing Django REST framework 

```
pip install djangorestframework
```
	
To work in the future with both frontend and backend side, in developing stage we migth use a cors headers library to allow traffic between servers

```
pip install django-cors-headers
```

> Don’t forget to added to INSTALLED_APPS list

```
INSTALLED_APPS = [
    ... 
    'corsheaders',
]
```

We have to add cors headers app to MIDDLEWARS list

If we create,  delete or update a model we have to perfom the next command to preparte migration to a project

```
Python manage.py makemigrations <app name> 
```

> It's optional if we want only migrate a specific app model. 

Then we have to execute this command to migrate all.  

```
python manage.py migrate <app name>
```

### Setup superuser

```
python manage.py createsuperuser <user_name>
```

To enable admin panel models, we have to add model to admin.py file:

```
admin.site.register(<app name>)
```
