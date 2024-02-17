# RESTfulness
# An API or application programming interface is a gateway to back-end data. 
# It allows you to easily access and modify this data, 
# And REST is an architectural style for designing APIs for your project. 
# It is hugely popular among developers because it's much easier to develop and implement 
# than other architectural styles.
 
# Easy to learn
# Quick to develop

# REST APIs provide an easy way for you to communicate with the server 
# and access the data that powers your application. 
# But an API is only RESTful if it complies with certain constraints.

# It must have 
# client-server architecture, 
# a REST API is always Stateless, 
# and it should be Cacheable. 
# It should be layered, 
# have a uniform interface 
# and it might also include code on demand,but this is optional. 

# client-server architecture:
# The API should use client-server architecture. 
# There should be a server that is serving the resources and there should be a client who consumes them. 

# Stateless:
# A REST API is Stateless, this means that the server does not contain any state of the API client 
# who is making the call so it cannot identify who is making the request or 
# what their previously requested data was without proper user information. 
# In fact, the State is only saved on the client machine, not on the server and this influences 
# what you should include in your API endpoints or URL Paths but more on this later. 

# Cachable:
# The API should also be Cacheable. 
# This means that responses can be saved by a web browser or a server or any system. 
# This caching process can help to reduce the server load by using the API result 
# from the cache instead of making an actual request to the server every time.

# Layered:
# Layered means that the entire system architecture can be split or 
# decoupled into multiple layers and you should be able to add or remove a layer at any time.
# Layers of a RESTful API system could include a Firewall Load balancer, a Web server, and a Database.

# uniform interface:
# This may sound a little confusing at this point, 
# but it means that the system should offer a uniform communication system to access the resources. 
# For example, there should be unique URLs for each resource. 
# There should also be a unified way to modify or proceed further with a resource from the API result 
# or representation in a standard XML or Json format. 

# code on demand (business logic,code that can run improve results):
# It means that the API may deliver some business logic or 
# code that the client can run to further improve the response result.

# example:To understand this code-on-demand feature, consider the following script tag 
# that loads some JavaScript code from an API endpoint of the Little Lemon Restaurant. 
# Once loaded this script can display any special menu items for that day. 


# Resources
# Resources are a core part of every REST API. 
# So, it's important for you to become familiar with how APIs present Resources. 

# example:
# Say the Little Lemon Restaurant has a mobile App 
# which can be used by customers and managers. 
# Managers can use the App to get information about orders and customers 
# while the customers use this App to browse the menu and place orders. 

# To support this, the App uses different APIs to fetch data from the server and in each case, 
# the resource type will be different.

# Let's explore a few examples. 

# API-1
# If a manager wants to see all orders, the App makes a call to the API little dot lemon forward slash orders and displays the result.
# The resource type in this case is a list of order objects.
# API-1--> https://little.lemon/orders
# Resource type : order object

# API-2
# If a manager wants to view more specific information about a particular order, 
# say the order with the ID 16, the App makes a call to the API little dot lemon forward slash orders forward slash 16. 
# The resource type is the order object.
# API-2--> https://little.lemon/orders/16
# Resource type : order object.

# API-3
# To see who placed the order, the App makes an API call with an extra filter forward slash customer. 
# This retrieves all the details about the customer of that order. 
# The resource type in this case is the customer object.
# API-3--> https://little.lemon/orders/16/customer
# Resource type : customer object.

# API-4
# Say the manager wants to look at what the menu items of order number 16 were, 
# the App makes an API call that replaces forward slash customer with forward slash menu items. 
# Only the menu items of order 16 will show on the result and 
# this time the resource type is the menu item object.
# API-4--> https://little.lemon/orders/16/menu-items
# Resource type : menu item object.

# API-5
# If the customer wants to browse the menu, 
# the App uses another API, little dot lemon forward slash menu items. 
# And although the resource type will also be the menu items object.
# API-5--> https://little.lemon/menu-items
# Resource type : menu item object.

# The return will be all available menu items of the restaurant. 
# But sometimes the resource type is the same although the result can be filtered to be more specific.

# API-6
# This time the customer wants to browse food items from a specific category say appetizers, 
# the App will add question mark category equal sign appetizers. 
# Notice that the endpoint is the same as the previous API but it filters the output to only appetizers. 
# For both cases, however, the resources still menu item object.
# API-6--> https://little.lemon/menu-items?category=appetizers
# Resource type : menu item object.


# REST API Constraint of Statelessness:
# You need to keep in mind that the server always represents only what you ask for. 
# It does not remember anything of what happened before. 

# For instance,if the manager retrieves the information about order 16 and then wants to look at the menu items of order 16, 
# (API-2--> https://little.lemon/orders/16)
# you cannot just send a follow-up HTTP request to the endpoint forward slash menu items 
# because (# API-5--> https://little.lemon/menu-items) this API will return all menu items and not just the menu items of order 16. 
# The server does not remember that your earlier call was for a specific order.


# If you want to get the menu items for a specific order number, 
# you need to explicitly supply that order number to the server # API-4--> https://little.lemon/orders/16/menu-items. 

# In simple terms, this is what Stateless means. 
# The server cannot recognize the client automatically. 
# API calls must include more information about the user. 