# Models:
# Django models are used to define the structure of stored data, including the field types and possibly also their 
# maximum size, default values, selection list options, help text for documentation, label text for forms, etc. 
# Each model is a Python class that subclasses django.db.models.Model. 
# Each attribute of the model represents a database field. 
# With all of this, Django gives you an automatically generated database-access API. 
# You can create a model in Django to store data in the database conveniently. 
# Moreover, you can use the admin panel of Django to create, update, delete, or retrieve fields of a model and various similar operations.
# Django models provide simplicity, consistency, version control, and advanced metadata handling.

# models.Model is django models is a class and Model is a subclass

# python manage.py makemigrations
# python manage.py migrate

# the database will be created the migration folder contain 0001_initial.py
# class migration will be create the class student code will be execute and it will be create database

# It provides the instruction to the database.
# the database table will created Apps_student
# Install sqlite extension
# and right click and open database now the sqlite explorer will display.
# ID field was automatically generated primary key for django
# If you keeps the model upto date and it reflects the actual database


# Model manager

# In oder to build a database interaction we first need to build a database
# Once we designed our databaase we create a django models models 
# models are implemented by creating a new class within our model we define fields and behaviour
# Models represents tables in our database
# Django provides a non sql approach a way to present the django orm instuction with the project
# database tables and data in our primary programming language python using django orm to perform some 
# operations on the database wouldn't be possible without the model manager.

# The model manager as interface provides access to the orm query tools  
# fields(student model) --> Queryset api(model manager) --> Database

# Django model we need to utilize the model information and interface with the orm toolkit the querysetapi
# for example through the model manager the query set api provides the toolkit for us to then build a query
# which can be executed on the database
# everytime we build a query within our django application we going to utilize or pass through
# the model manager to access the querysetapi tools


# display all data from database: Retrieve object from the database
# student.objects.all()-> student(model).object( defaut manager).all()->quersetapi method

# every model has access to the querysetapi every model is assigned a default module manager called ojects

# Roles
# Interface -> model manage is doorway an interface that provides access django orm features
# Querysetapi -> model manager provides access to the querysetapi is used to query the database
# and return data from a database
# objects -> Django models have one or more model maangers each model will have model manager signed
# by default called objects.
# Modify data returned from database -> We can add multiple mode managers It can be extended to provide
# customization which might for ex: modify data return from the database
# 