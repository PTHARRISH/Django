# Introduction of API:
# Nearly all of us have interacted with an API before, even if we don't know it. 
# If you've checked the weather on your phone or if you've ordered food online, then you relied on an API 
# to give you access to another app's functionality or to retrieve information for you. 
# In fact, most of today's web applications rely on APIs to work. 
# An API or Application Programming Interface is a gateway to back-end data. 
# APIs allow different apps and services to exchange information or allow access to functionality, 
# and as the use of mobile and other technologies increases, so too does the demand for APIs. 


# API used in the Real world:
# What is an API ?:
# APIs are essentially the bread and butter of end-to-end full-stack developments.
# I say bread and butter just because they're so crucial in terms of describing 
# how software components interact with each other.

# what do API do?
# Whenever you pull up your Instagram app, you are interacting with APIs all over the place. 
# There's a specific set of APIs that renders things like stories and photos and videos in your home feed. 
# There's another API that does the same thing, but on your explore page. 
# There's another API that registers things like double-taps on a post, as likes on the back end, 
# and that tells your device to render that little heart icon in the red color.

# An API as a bank teller, and the data the back-end services host as the money in the bank. 
# When you are a customer wanting to withdraw or deposit money from the bank, 
# you're not necessarily interacting with the money directly. 
# Instead, you go to a bank teller, in this case, an API, which handles things like communications 
# between the end user and the back-end services, and also tells you how much money or data you're able to access. 

# How are APIs designed at Meta ?
# Typically, the actual API design is a handshake agreement between several engineers. 
# Typically, back-end and front end engineers agree on the API structure. 
# They also agree on things like what the request structure could look like and 
# what the response could look like as well.

# What do you consider when designing an API?
# To consider is also who are the people who are going to be accessing the data, 
# and also your API and services. 
# You want to make sure that you add a layer of security in the form of credentials to your request 
# in order to preserve that integrity as well.

# Who want to better understand APIs?
# When you're building an API, you really have to think about components as part of a larger piece.
# There is beauty in having an output that is reflective of things that you see in application in the real world. 
# Have fun with it, brainstorm with engineers, and get a sense of what the target architecture for an API could be.


# What you know about HTTP?
# HTTP stands for Hypertext Transfer Protocol, 
# and that it's one of the most widely used communication protocols for transferring data across the Internet. 
# When you browse webpages, view images, or submit a form, 
# your data is transmitted using HTTP or a secured version of it, which is called HTTPS. 

# How does that transmission work for HTTP and HTTPS respectively?
# HTTP:
# Communicating over HTTP requires at least two parts: 
# the client who requests some information and the server who responds to this request and serves the content.

# HTTPS:
# HTTPS is the secured version of HTTP, which makes it better suited to instances where security is a concern. 
# With HTTPS, the client's computer encrypts data before it starts its journey to the server. 
# The server then decrypts this client-side data and processes it.
# But the web server also encrypts the response data and sends the encrypted content back to your browser. 
# Your browser then decrypts the response and displays it. 
# Since the content is encrypted, it is more secure and very difficult to steal or retrieve information from it. 
# For submitting sensitive data, like credit card information, 
# it is always preferable to use HTTPS to make sure the data is secure.

# HTTP methods:
# HTTP methods are also called HTTP verbs. 
# There are five methods commonly used when accessing content over HTTP. 
# They are: 
#   GET, which retrieves a resource; 
#   POST, used to send data to the server and then create a record; 
#   PUT, which updates the whole resource; 
#   PATCH, which are used to partially update a resource; 
#   DELETE, which deletes a resource.

# HTTP request:
# It contain different types of information that a user's browser sends as encoded data. 
# A typical HTTP request includes the following, HTTP version type, 
# for example, 1.1 or 2.0, URL or path, HTTP method, HTTP request headers, and an optional HTTP body. 

# what are the HTTP request headers and body again?
# when you submit a form like your username and password to sign into a website, that data is passed 
# to the web server as the HTTP body as either a raw JSON string or a form URL encoded string. 
# HTTP headers, on the other hand, are a core part of every HTTP request 
# and may contain extra information that helps the server make some decisions on how to present the content.

#  Examples of HTTP request headers are cookies, user agents, and referrers.

# HTTP response:
# It consists of information that the browser uses to properly display the content and the response body. 
# The response contains the resource that was requested. 
# It also contains information like the length of the content, the content type, and headers like cookies.
# It also contains ETags, the time when the content was last modified, and finally, 
# the response also contains some special numerical codes called HTTP status codes.

# HTTP Status Code:
# they are not really messages addressed to you, the user. 
# They actually provide extra information to your browser about the resource. 

# For example, if everything is okay, the server sends 200.
# You will not be aware of this because it doesn't even display in your browser. 
# Or if the requested content can't be found, the server responds with the 404 error code, 
# which usually displays in the browser because there was nothing else to show. 

# Here is a range of error codes and their meanings. 
# 100-199 are used for informational messages. (102 – Processing )
# 200-299 are successful responses, (200 – Successful,201 – Created)
# 300-399 provides redirection information, (301 – Permanently moved)
# 400-499 are client error responses,(400 - Bad Request, 401 - Unauthorized, 403 - Forbidden, 404 - Not Found)
# 500-599 are server error codes.

# Server errors are usually raised when the server-side code lacks proper error checks in the code, 
# configuration mismatch, incorrect package dependencies, and so on. 

# The client-side errors usually occur when the client makes a bad API request 
# with insufficient information in the request body or 
# when the client requests a resource that is not present on the server. 
# But take note that sometimes the same status codes can convey different messages in different contexts.

# For example, a 200 status code for a GET request means the content was found. 
# The same 200 code for a PUT request means that the data transmission and update process was successful. 
# Similarly, for a DELETE request, this 200 status code means that the resource was successfully deleted. 
# Some of the most used status codes are 200 and 201, 303 and 304, 400, 401, 403, and 404, as well as 500.


# Status code range

# 100-199
# This range is mainly used to pass on some information. 
# For example, sometimes an API needs time to process the request and it can’t instantly deliver the result. 
# In such a case, the API developer can set it to keep returning 102 – Processing until the result is ready. 
# This way, the client understands that the result isn’t ready and should be checked again.

# 200-299
# These are the success codes. 
# If the client requests something and the API acts successfully, it should deliver the output with one of these status codes.  
# For example, for a  PUT, PATCH, or DELETE call, you can return 200 – Successful if the operation was successful. 
# For a successful POST call, you can set it to return a 201 – Created status code when the resource has been created successfully.  

# 300-399
# These are the redirection codes. 
# Suppose as an API developer, you changed the API endpoint from /api/items to api/menu-items. 
# If the client makes an API call to /api/items, 
# then you can redirect the client to this new endpoint /api/menu-items with 
# 301 – Permanently moved status code so that the client can make new calls to that endpoint next time.  

# 400-499
# 4xx status codes are used in the following situation: 
# if the client requests something that does not exist, sends an invalid payload with insufficient data, 
# or wants to perform an action that the client is not authorized for.
# For the above scenarios, the appropriate status codes will be:

# 404 - Not Found if the client requests something that doesn’t exist,

# 400 - Bad Request if a client sends an invalid payload with insufficient data,

# 401 - Unauthorized,

# 403 - Forbidden if the client tries to perform an action it's not authorized for.

# 500-599 -These alarming status codes are usually automatically generated on the server side if something goes wrong in the code, 
# and the API developer doesn't write code to deal with those errors. 
# For example, a client requests a non-existing resource, 
# and the API developer tries to display that resource without adequately 
# checking if that resource exists in the database. 
# Or if the API developer didn't validate the incoming data and attempted to create a new resource with invalid or insufficient data. 
# You, as an API developer, should always avoid 5xx errors.  


