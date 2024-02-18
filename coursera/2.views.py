# Views
# In Django, a view is a function designed to handle a web request and return a web response 
# such as an HTML document. 
# HTTP request response scenario using an example of a static file and a dynamic file. 
# For a static file with no dynamic content, 
# the HTTP request just needs to map to where the file is located and return that page for rendering. 
# As the static page does not change, nothing else is needed. 

# You create the function inside the views.py file and return the HTML. 


# request:
# First, you import the class HTTP response from the django.http module. 
# Next, you define a function called home, and this is known as the view function. 
# Each view function takes an HTTP request object as its first parameter named request

