
# What is a web framework?
# Frameworks are designed to support the developer in building the web application. 
# The purpose of a web framework is to make application development easier and to provide the developer 
# with a clean structure that keeps things in order and allows for changes and modifications. 
# Frameworks also allow for code reusability facilitated by existing code. 
# When building a web application, it's important to understand that many different pieces and components exist. 

# For example, you can build a static website with just some HTML, CSS, and JavaScript. 
# However, suppose you want to add e-commerce functionality such as a shop. 
# In that case, you will have to implement things like user sign-in, payment transactions, security performance, 
# and deal with data being posted from web forms. 
# This will require your application to split into two parts, the front-end and the back-end.
# The front end is the part of the website the user interacts with via the web browser, 
# and the back-end is the part that runs on a web server and usually contains the database. 
# If your website requires functionalities such as e-commerce, site users, payment processing, 
# and data stored in a database, it will most likely need a back-end, more specifically, 
# a back-end application to manage that back-end.

# One of the most popular is Django. 
# Django is a high-level free, open source Python web framework that encourages rapid development and clean pragmatic design. 
# It's built by experienced developers and takes care of many of the tasks associated with web development, 
# allowing you to focus on writing your app without needing to reinvent the wheel. 

# Let's explore some of the benefits of using the Django framework. 
# This includes speed, features, security, and scalability. 
# According to the developers of Django themselves, 
# Django is ridiculously fast and speeds up the process by reducing the amount of code to be written. 
# This means that you can take applications from concept to completion as quickly as possible. 
# Django is feature-rich and includes many right out of the box features 
# that you can use to handle common web development tasks. 
# These include tasks such as user authentication, content administration, sitemaps, and RSS feeds. 
# Django is very secure and helps developers avoid many common security mistakes. 
# It provides a secure layer of internal middleware that protects it from common attacks attempting 
# to steal information. 
# Finally, Django is highly scalable. 
# It allows data to be stored on other servers than the one in use without too many changes in configuration. 
# This provides flexibility and speed, and as a result, some of the busiest sites on the web leverage 
# Django is ability to quickly and flexibly scale. 
# Now you have a basic understanding of what a web framework is and 
# why the Django framework is a popular choice for application development. 


# The three-tier architecture:
# Architecture refers to the fundamental structures of a software system. 
# Modern applications tend to be built in what is called the three-tier architecture. 
# This is a modular based approach to client-server architecture that splits the application into three logical parts,
# a presentation tier and application tier, and a data tier. 

# The presentation tier is the layer the users primarily interact with through user interfaces from their desktop, 
# laptop, or mobile devices. 
# It's commonly built with a UI framework or library such as React from Mehta, 
# and it communicates with the other tiers by sending results through the application interface. 

# The data tier usually consists of database servers for storing and retrieving information. 
# A dynamic website needs to be able to store and retrieve data. 
# A database is the best choice as it stores data in tables or objects depending on the choice of database. 

# The application tier is what ties in the other two tiers. 
# It gets data from the presentation layer and persisted in the data tier. 
# It's important to note that these parts are logical enough physical, meaning, 
# you can have all three tiers running on the same web server.


# MVC Architecture
# Most of the web frameworks implement the MVC (Model-View-Controller) architecture. 
# The MVC design pattern separates the entire web application development process into three layers, 
# Model, View and Controller. 

# The following diagram explains the interplay of these three layers.
# Diagram for model-view-controller architecture layers
# In the MVC approach, the controller intercepts the user requests. 
# It coordinates with the view and model layers to send the appropriate response back to the client.
# The model is responsible for data definitions, processing logic and interaction with the backend database.
# The view is the presentation layer of the application.
# It takes care of the placement and formatting of the result and sends it to the controller, 
# which in turn, redirects it to the client as the application's response.

# MVT Architecture
# The Django framework adapts a Model, View and Template (MVT) approach, a slight variation of the MVC approach.
# Here too, the model is the data layer of the application. 

# The view is, in fact, the layer that undertakes the processing logic.
# The template is the presentation layer.
# Diagram for model-view-template architecture layers
# A Django application consists of the following components: 

# URL dispatcher 
# View 
# Model 
# Template 


# URL dispatcher
# Django's URL dispatcher mechanism is equivalent to the controller in the MVC architecture.
# The urls.py module in the Django project's package folder acts as the dispatcher.
# It defines the URL patterns. 
# Each URL pattern is mapped with a view function to be invoked when the client's request URL is found 
# to be matching with it.
# The URL patterns defined in each app under the project are also included. 
# Here’s the urls.py file in the app folder.

# urls.py
# from django.urls import path 
# from . import views 

# urlpatterns = [ 
#     path('', views.index, name='index'), 
# ] 

# When the server receives a request in the client URL, the dispatcher matches its pattern 
# with the patterns available in the urls.py. 
# It then routes the flow of the application toward its associated view.


# View
# The view function reads the path, query, and body parameters included in the client's request If required, 
# it uses this data to interact with the models to perform CRUD operations.
# A view can be a user-defined function or a class.
# You create View definitions in the views.pyfile of the respective app package folder. 
# The following code in the view.py file defines the index() view function.

# Views.py
# from django.shortcuts import render 
# from django.http import HttpResponse 

# def index(request): 
#     return HttpResponse("Hello, world.") 


# Model
# A model is a Python class.  
# An app may have one or more model classes, conventionally put in the models.py file. 
# Django migrates the attributes of the model class to construct a database table of a matching structure.
# Django's Object Relational Mapper helps perform CRUD operations 
# In an object-oriented way instead of invoking SQL queries.
# The view uses the client's and the model's data and renders its response using a template.


# Template 
# A template is a web page containing a mix of static HTML and Django Template Language code blocks.
# You place Template web pages in the templates folder with the .html extension.
# Django's template processor uses any context data from the view inserted 
# in these blocks to formulate a dynamic response.

# The view, in turn, returns the response to the user.
# This explains how Django's MVT architecture handles the request-response cycle in a web application.


# ----------------------------------------------------------------------------------------------------------------------------------------------