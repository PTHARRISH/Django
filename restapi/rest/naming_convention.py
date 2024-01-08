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
