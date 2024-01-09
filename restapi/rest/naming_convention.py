# Naming conventions
# By now you know the importance of API endpoints and 
# how they determine precisely what data the server will send to your app. 
# But a well-designed endpoint also conveys valuable information about its purpose, 
# which is helpful for developers and the project itself in the long run. 
# Your REST APIs Uniform Resource Identifier or (orders/16/menu-items)
# URI is one of the first things that users will notice when a page loads.
# It is also called an endpoint or URL path.(orders/16/menu-items)

# First impressions always make a big difference and that is why naming conventions for APIs are important. 

# Endpoint name
# https://little.lemon/orders
# Say the Little Lemon restaurant menu app needs APIs to display all their orders. 
# A suitable API endpoint is forward slash orders spelled with a lowercase o 
# and not orders spelled with an uppercase O. 
# So, your API endpoint should always use lowercase letters and hyphens to separate multiple words.

# Using underscores or snake case, 
# title case or camel case, 
# two separate words is not optimal because it makes the names difficult to read and understand.

# There is an exception to the camel case rule though if you're API accepts a variable, 
# for example, a userId or orderId you should always represent them in camel case and wrap them in curly braces.


# For example, if you want to create an API for a specific order, 
# it should be forward slash orders forward slash open curly brace order Id with a capital I close curly brace. 
# Specific orders -> order/{orderId}

# By adding forward slash menu hyphen items to the API endpoint, you can fetch the menu items for a specific order. 
# menu item of Specific orders -> order/{orderId}/menu-items

# you can fetch orders of a specific customer by changing the Id to customerId 
# wrapped in curly braces and adding forward slash orders.
# order of specific customer -> order/customer/{customerId}/orders

# that the API endpoints contain two different variables, 
# orderId and customerId.
# orderId -> order/{orderId}/menu-items
# customerId -> customer/{customerId}/orders
# And they are both denoted by wrapping them in curly braces and writing Id with a capital I.
# Also, always try to use clear, concise, and meaningful words in your API names to make them easy to read right away.

# use of forward slashes. 
# If your project has related objects, you should use forward slashes in your API URIs to indicate their hierarchical relationship. 

# An example of such a hierarchy is, a customer can have orders with order items in a restaurant API project. 

# Another example is a library can have books with authors. 
# So, to get the author of a particular book, you can use the API endpoint, library forward slash books forward slash and then bookId
# wrapped in curly braces, and finally forward slash author. 
# Or to get all books written by a particular author, you can use an Id for the author instead and add forward slash books.

# author of a book: /library/books/{bookId}/author
# all books by an author: /library/authors/{authorName}/books

# Nouns
# Another naming convention is that your API should always use a noun to indicate the resources it is dealing with. 
# An API that returns a collection of books or a book should use the nouns \books or books and bookId wrapped in curly braces(books/{booksId}).
# Similarly, to get the price of a book, you should use the nouns books, bookId price(books/{booksId}/price). 

# Bad API Names
# API endpoints with verbs like getAllBooks or getUser userId are examples of bad API names. 
# ex: /getAllBooks,/getUser/{userId}
# That's because the resources and a REST API endpoint should be always represented with a noun and never with a verb. 
# API endpoints such as users, userId, delete or orders, orderId, save are also wrong 
# because they use HTTP requests as verbs to indicate the action the API performs. 

# HTTP methods
# DELETE --> /users/{userId}
# you should send an HTTP DELETE request to users, userId to delete a user. 

# PUT --> /orders/{orderId}
# PATCH --> /orders/{orderId}
# And you should send an HTTP PUT or PATCH request to orders, orderId to update the order. 

# CRUD
# Endpoints that use standard CRUD operation names such as create, read, update or delete should be avoided for two reasons, 
# the resources these endpoints represent should be nouns, 
# and the appropriate HTTP requests like GET, POST, PUT, or DELETE should be used with those endpoints to perform the necessary manipulations. 

#  Something else to consider is whether file names should be used in APIs, the restaurant API project can return API results as XML and Json data. 

# So, the question is, can you design your endpoints as orders orderId.json to get the Json data? Or perhaps orders orderId.xml for XML data? 
# No, you should never use a file name extension in your API. 
# To solve this problem, you should accept the expected data format as a query string parameter.

# Query String Format
# if you want the output in a Json format, 
# you can add question mark format, equal sign Json to the API endpoint. 
# And for XML, you can use a question mark, format, equal sign xml at the end.
# example:
# /orders/{orderId}?format=json
# /orders/{orderId}?format=xml


# Minified version of JavaScript file
# Similarly, to deliver a minified version or source version of a JavaScript file, 
# you use API endpoints like /assets/Js/ jquery/3.6.0/min. Or /assets/js/moment/2.29 .4/original. 
# But what if you need to filter a collection or perform a search? 

# For instance, the Little Lemon restaurant has many items on its menu but you are only interested in appetizers, 
# to filter the results, you should always accept the data as a query string parameter. 
# In a URL everything you send after a question mark is a query string.

# Query String parameter
# /menu-items
# the API endpoint menu items, returns all menu items

# /menu-items?category=appetizer-> query string
# but to only get the appetizers, you should pass the category name to the endpoint as question mark category equal sign appetizer.


# /menu-items?category=main
# /menu-items?category=dessert-> query string
# Consequently, 
# if you design APIs that can be filtered this way, other developers on your team will derive that to get a list of mains or desserts 
# they can change the endpoint to question mark, category, equal sign main or question mark category, equal sign dessert.


# Trailing slash
# Another best practice is that when you share your API endpoints with your team or the public, 
# you should never add a trailing slash to the end of the API endpoint. 
# What this means is that API names that end with a forward slash, like orders, orderId, and curly braces followed by a forward slash is bad practice. 
# So is sports basketball teams followed by another forward slash at the end. 
# Simply end the API without the forward slash at the end.

# Don't add forward slash at the end:
# /orders/{orderId}/
# /sports/basketball/teams/

# Use API like this:
# /orders/{orderId}
# /sports/basketball/teams
