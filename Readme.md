## What is Django?
Django is a Framework
# what is a Framework?
Framework has some patterns created and we will fill the gaps 
- Framework is the implementation of several tasks and give developers a structure for application development. Each framework comes with its own collection of modules or packages that significantly reduce development time._
 
# Framework vs Library

## **Backend**  
- API - send request and response
- Auth 
- session
- Database
- middlewares

## Python 

* Flask - easier to start [Library]
* Django - a big initial learning curve [Framework]
* Fast API - a bit more learning curve [Library]

## Tools 
* Pycharm 
* Postman
* python

## What is venv?
-



* **PYPI - Python Package Index**

## python -m manage --help 
- "-m" refers to module

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

### [auth]
1.     changepassword
2.     createsuperuser

### [contenttypes]
1.     remove_stale_contenttypes

### [django]
1.     check
2.     compilemessages
3.     createcachetable
4.     dbshell
5.     diffsettings
6.     dumpdata
7.     flush
8.     inspectdb
9.     loaddata
10.     makemessages
11.     makemigrations
12.     migrate
13.     optimizemigration
14.     sendtestemail
15.     shell
16.     showmigrations
17.     sqlflush
18.     sqlmigrate
19.     sqlsequencereset
20.     squashmigrations
21.     startapp
22.     startproject
23.     test
24.     testserver

### [sessions]
1.     clearsessions

### [staticfiles]
1.     collectstatic
2.     findstatic
3.     runserver


### SETTINGS 
* helps to customize django application
* The setting has 
1. DEBUG = True which allows to run the application
2. DEBUG = False 
 - **CommandError:** You must set settings.ALLOWED_HOSTS if DEBUG is False.
 - When we set DEBUG = False and 
   ALLOWED_HOSTS = ['localhost'] it will run the application and shows response as BAD REQUEST when we open the localhost:8000
    
* Django architecture works on the thought process of applications.
[ combination of apps ]
* sqlite3 is a file based database and stored in BASE_DIR/db.sqlite3
* We can change database at DATABASES variable in settings file.
* It supports all relational and some non-relational database.

# What is middleware?
- Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output.

- Each middleware component is responsible for doing some specific function.

* **CSRF - Cross Site Request Forgery**

* The **_makemigrations_** command looks at all your available models and creates migrations for whichever tables don’t already exist. 
* **_migrate_** runs the migrations and creates tables in your database, as well as optionally providing much richer schema control.

### python -m manage migrate 
- to change the schema
- creation of tables , adding primary key and columns

### python -m manage showmigrations


### python -m manage createsuperuser


#### View 
- It will tell what to respond for a request.

- URL pattern is like mapping routes to views.

1. Can we multiple views for a single request?
- No,
e.g; `path('', say_hello),
    path('', say_bye),`

2. Dunder init
3. 


#### Creating an application
* python -m manage startapp firstapp

* ##### **ORM - Object Relational Mapper**



### Why does admin panel exist?
- eg; Amazon support they need to go their platform and they ask details and they have some of searching information.
- Should amzon create a complete website for internal working as well.

**Headless CMS :**
- CMS = Content Management System