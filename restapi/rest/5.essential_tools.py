# Essential tools
# If you want to work quickly and efficiently as a developer, you need the right tools. 
# For example, an intelligent code editor can help you develop more rapidly and become more competent. 

# APIs Tools

# curls
# First is curl, a well-known tool for developers who want to make HTTP calls from the command line. 
# It is available for all major operating systems, but it doesn't have a graphical tool. 
# To use curl, simply open your PowerShell in Windows or the terminal and Linux or macOS, 
# 1. curl
# type curl and hit "Enter". 
# Curl makes it easy to send HTTP GET requests. 
# For example, simply add the API URI after curl. 
# 2. curl https://postman-echo.com/get?project=LittleLemon
# This command sends a HTTP GET request to Postman Echo, a service from Postman to display the headers and request body sent to it. 
# Pretty useful for testing API calls. 
# It works slightly differently for a POST request.

# curl -d "project=LittleLemon" -X POST https://postman-echo.com/post
# This time, add to the request body using hyphen d and the HTTP method name, which is POST, preceded by hyphen X.

# Postman
# Postman, which has cross-platform desktop tools that make it easy to test and debug APIs. 
# With an advanced graphical interface and a web version, 
# Postman is a powerful tool for API development. 
# With Postman, you spend less time fiddling with API details and more time building the perfect API.


# Insomnia
# Insomnia REST Client, a powerful REST API client used to store, organize, and execute REST API requests. 
# Insomnia is free, cross-platform, and comes with a very user-friendly interface. 
# You can download and install insomnia

# How to use Insomnia
# Insomnia is a great tool for playing with APIs. 
# All requests in Insomnia will be saved in a request collection. 

# To get started, click on the Create button in the top right corner and select Request collection.
# Give it a name like first collection and click on Create. 
# Now you are inside an empty collection. 
# To create your first API request, click on the Plus icon on the left sidebar and select HTTP Request. 
# You can also do this by pressing Command plus N on macOS or Control plus N in Windows and Linux. 
# You can double-click on the default request name, new request, and change the name to something more personal, like first request.
# At the top of the middle section where it says GET, you can click and select the type of HTTP method your request is going to be. 
# Leave it as GET for now. 
# In the text box next to it, 

# GET:
# write your API URL, httpshttpbin.org/get?project=LittleLemon. httpbin.org is a free service that allows you to experiment with different types of HTTP methods.
# When you call one of these APIs, it prints back what you sent to it. 
# Now hit the Send button on the right and you will see that httpbin has returned the same query argument you sent to it, which in your case was project is equal to LittleLemon. 

# POST:
# This time let's try making a new HTTP POST request. 
# To do this, click on the Plus icon in the left sidebar and select HTTP Request. 
# Once the request is created, double-click on its name and give it a new name, such as second request. Now click on the HTTP method drop-down and 
# select POST and this time add httpshttpbin.org/post in the URL field

# A HTTP POST request accepts arguments as form data or JSON data. 
# With Insomnia, you can easily input data for a POST request by clicking on the body tab and selecting Form URL Encoded or JSON. 
# Here in this argument window, you can finally layout all your arguments in an easy to use and organized manner. 
# On the left, you can write the argument name and on the right, the value. 
# Write project in the argument field and LittleLemon as the value. 
# Now click on the Send button to display the output. 