# Project and file structures
# Django file structures:
# In basic webpage HTML is used for basic page structure,CSS for the look and style, and JavaScript for client-side interaction.
# Suppose you are creating a static website, the project structure may only need some CSS, JavaScript, and image folders
# This approach may work fine for a simple static website.
# The purpose of the project structure is to lay out the files in a way that makes them easy to update. 
# when dealing with web applications requiring more complex functionality, such as the need to hold state or access and store data, 
# things need to be set up differently. 

# Using a framework, developers can focus on creating functionality unique to the projects, instead of repeating 
# the repetitive coding tasks associated with building a web application. 
# Django was created by developers who have followed best practices. 
# It allows you to set up your web application in a structured way for easier development.
 
# Django framework, it's good to fully understand what is usually required to create a dynamic web application. 
# This can involve working with Internet protocols, web server configuration, and data retrieval, or storage.


# HTTP
# HTTP is essential in web development as every action is always tied into a HTTP request, pointing to some URL. 
# A web server is required to get the page users want and return it to them via HTTP. 
# Django comes with its own development server, which is written in Python. 
# This will save the developer a lot of time and avoid any messy configurations. 
# That the web is stateless, meaning it does not store anything for future reference. 
# A database is required to keep and retrieve the data associated with the website. 

# For example: every time a user submits a form on a site, this data will need to be stored 
# so it can be retrieved and rendered later. 


# Django Project:
# In Django, a project represents the entire web application. 
# Create a django project --> ( django-admin startproject projectname . )
# Django provides a set of commands that auto generates a project structure that contains the configuration 
# and setting related to the entire web application.
# Django project is a way to organize your Python files and folders.
# This allows developers to focus on code rather than configuration.

# Apps:
# In Django, an app is a sub-module of a project. 
# It is typically used to implement functionality for some specific purpose.
# Apps can be self-contained, meaning they do not rely on other apps to function. 
# As a result, they can be used or reused in many different projects. 
# This leads nicely to the don't repeat yourself, DRY principles. 
# Write once but use it many times. 
# Just remember that a Django web application is a project that contains many apps.

# For example, suppose you are creating a social media application. 
# Well, in Django, the social media application would be the project, 
# and the different features would be represented by the different apps. 
# You could create separate apps for the news feed, the comments, the friends list, the user page, and so on. 

# Apps are added using the start app command. ( python manage.py startapp feed )

# For Django to recognize an app in a project, it must be added to the installed apps setting. 
# Django app is a set of code that interacts with various parts of the framework. 
# There are a few places where Django needs to interact with installed applications.(settings.py->Installed_apps['app_name']) 
# This is mainly for configuration and introspection. 
# That's why the application registry maintains metadata in an app config instance for each installed application. 

# Applications usually include some combination, such as models, views, templates, template tags, static files, URLs, and middleware



# Project package:
# The startproject command option of the Django-admin utility creates the folder of the given name, 
# inside which there is another folder of the same name. 
# For example, the command: django-admin startproject demoproject
# This creates a demoproject folder, inside which there’s another demoproject folder.
# The inner folder is a Python package. For a folder to be recognized by Python as a package, it must have a file __init__.py. 
# In addition, the startproject template places four more files in the package folder.

# settings.py:
# Django configures specific parameters with their default values and puts them in this file. 
# The django-admin utility and manage.py script use these settings while performing various administrative tasks.

# urls.py:
# This script contains a list of object urlpatterns. 
# Every time the client browser requests a URL, the Django server looks to match its pattern and routes the application to the mapped view. 
# The default structure of urls.py contains a view mapped to the project’s Admin site.

# urls.py:
# from django.contrib import admin 
# from django.urls import path 

#  urlpatterns = [ 
#     path('admin/', admin.site.urls), 
# ] 

# asgi.py:
# This file is used by the application servers following the ASGI standard to serve asynchronous web applications.

# wsgi.py:
# Many web application servers implement the WSGI standard. 
# This script is the entry point for such WSGI-compatible servers to serve your classical web application. 

# settings.py:
# This file defines the attributes that influence the function of a Django application. 
# The startproject template assigns some default values to these attributes. 
# They may be modified as per requirement during the use of the application.
# Let us explain some critical settings.

# INSTALLED_APPS:
# This is a list of strings. 
# Each string represents the path of an app inside the parent project folder. 
# The startproject template installs some apps by default. 
# They appear in the INSTALLED_APPS list.

# settings.py:
# INSTALLED_APPS = [ 
#     'django.contrib.admin', 
#     'django.contrib.auth', 
#     'django.contrib.contenttypes', 
#     'django.contrib.sessions', 
#     'django.contrib.messages', 
#     'django.contrib.staticfiles', 
# ] 

# This list must be updated by adding its name whenever a new app is installed. 
# For example, if we create a demoapp with the following command: python manage.py startapp demoapp
# Then, add the 'demoapp' string inside the INSTALLED_APP list.
# Display of demoapp inside the installed app lis

# Databases:
# This attribute is a dictionary that specifies the configuration of one or more databases 
# to be used by the current Django application. 
# By default, Django uses the SQLite database. 
# Hence, this setting has a pre-defined configuration for it.

# DATABASES = { 
#     'default': { 
#         'ENGINE': 'django.db.backends.sqlite3', 
#         'NAME': BASE_DIR / 'db.sqlite3', 
#     } 
# } 

# The default name of the SQLite database is db.sqlite3, which is created in the parent project folder. 
# In place of SQLite, you may choose to use any other. 
# For example, for MySQL, the database settings could be as follows:

# settings.py:
# DATABASES = {   
#     'default': {   
#         'ENGINE': 'django.db.backends.mysql',   
#         'NAME': 'djangotest',   
#         'USER': 'root',   
#         'PASSWORD': 'password',   
#         'HOST': '127.0.0.1',   
#         'PORT': '3306',            
#     }   
# } 

# Note here the default port number for MySQL is 3306 as against the default port number 8000 used with SQLite in Django. 

# DEBUG = True
# By default, the development server runs in debug mode. 
# This helps develop the application as the server picks up changes in the code and the output can be refreshed without restarting. However, it must be disabled in the production environment.

# ALLOWED HOSTS
# This attribute is a list of strings. 
# By default, it is empty. 
# Each string represents the fully qualified host/domain where this Django site can be served. 
# For example, to make the site running on localhost externally visible, you may add 0.0.0.0:8000 to this list.

# ROOT_URLCONF
# This setting is a string pointing toward the urls.py module in which the project’s URL patterns are found. 
# In this case, it would be:

# ROOT_URLCONF = 'demoproject.urls'

# STATIC_URL:
# This setting points to the folder where the static files, such as JavaScript code, CSS files and images, are placed. 
# Usually, it is set to 'static/' corresponding to the folder of this name in the parent project folder.

# Test the installation
# After creating the project, to verify that it is built correctly, 
# start the development server with the following command while remaining in the project’s parent folder:

# python manage.py runserver

# Development server display with runserver code
# The server starts running at port 8000 of the localhost with IP address 127.0.0.1. Open the browser and enter 
# http://127.0.0.1:8000/


# Django page browser display
# If you get this output, the project has been created successfully.
# In this reading, you learned how to create a Django project. 
# The file structure of the project has also been explained here. 
# In the end, the installation of the project has been successfully verified.

# ----------------------------------------------------------------------------------------------------------------------------------------------
