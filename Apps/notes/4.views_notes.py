# Views:
# If you are building a basic static website, all you need to do is upload your website files to a web server. 
# However, if you're building a dynamic website using a framework, 
# you may need to get a retrieved data and render it to the browser. 
# This data could be anything like the user's name or a list of information.

# In Django, you use something called a view to create the logic to present data to the end-users. 
# how developers use them to process HTTP requests and return an HTTP response. 
# In Django, a view is a function designed to handle a web request and return a web response such as an HTML document.

# HTTP request response
# HTTP request response scenario using an example of a static file and a dynamic file. 

# Static file:
# For a static file with no dynamic content, 
# the HTTP request just needs to map to where the file is located and return that page for rendering. 
# As the static page does not change, nothing else is needed. 
# Suppose the page is at the address of littlelemon.com/index.html, 
# the web server will process the request and return a response containing the page index.html to the browser, 
# which then renders the content. 
# You may recall that this process is known as the HTTP request response cycle. 

# Dynamic file:
# In Django, you need to write a Python function to create something called a view. 
# You create the function inside the views.py file and return the HTML.
# First, you import the class HTTP response from the django.http module. 
# Next, you define a function called home, and this is known as the view function. 
# Each view function takes an HTTP request object as its first parameter named request. 
# As this is a Python function, it's possible to define more parameters and pass arguments, 
# It's important to know that the name you give the view function doesn't matter, 
# the function doesn't need to be named in a certain way for Django to recognize it. 


# create home view function: 
# In this example, it's called home because defining a function name that clearly indicates 
# Next, you create a variable and use it to store a string containing the HTML to be returned. 
# Once again, you can name this variable anything you want. 
# In this example, it's called content. 
# Finally, you need to return this variable containing the code, 
# and you do this by using the return statement with the HTTP response object. 
# Inside the HTTP response, you place the variable. 
# You can also perform other programming logic inside of view functions 
# such as processing data for emails and forms, retrieving data from a database, transforming data, 
# and rendering templates.

# It's important to know that creating a view function is not enough to make the request response work. 
# The view function needs to be mapped to a URL so when the request to the URL is made, the view function gets called. 
# This process of mapping a URL to a view function is known as routing. 
# To set up this routing to map URLs to views, you will need to create a new file. 


# url routing to view function:
# Inside your project app, create a new file called urls.py.
# You may recall that the project has a file with this name also.
# You will learn about the difference between them later. 
# Inside the urls.py file of the app, you first import the path function. 
# Then from the app directory, you import the views.py file. 
# Notice that both files are in the same directory. 
# You only need to place the period symbol after the import statement. 
# Next, to create a route and map a URL to a view, you need to create a list sequence using the variable, URL patterns. 
# This variable is assigned to a list that contains the URL paths that you want to create inside the app. 
# The URL patterns list can contain multiple paths, and each path is created using the path function.
# The function can accept arguments and two are acquired. 
# The first argument is the route, which is a string that contains a URL pattern, 
# and the second argument is the view, which contains the relative path and the name of the view function. 
# In this example, the view function is called for the homepage of the app. 
# For now, it's set to an empty string. 
# view functions and how developers use them to process HTTP requests and return an HTTP response. 
# view functions are mapped to URLs using the path function in the urls.py file of the app.