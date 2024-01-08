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

