# REST:
# Creating a REST API is straightforward. 
# But to make it robust, reliable, and perform well under loads, you need to spend time planning the architecture.

#KISS:
# KISS, which stands for keep it simple, stupid. 
# What this means is that you shouldn't try to perform too many tasks with one API. 
# A single API should do one specific job and do it well. (one API - one Job)

# For example, 
# for the Little Lemon project, the manager needs to update the item of the day, 
# and you want to make this easier for him by creating a new API.  

# One approach is to let the API determine what the previous item of the day was, 
# and to remove that status from the item. 

# And then it has to randomly pick one item based on some criteria and set its status as the new item of the day. 
# But this is asking the API to do too many things. 
# And if you randomly pick an item, it might not actually be the most popular item that day, right? 
# A better approach is to create only one API which updates the menu item.

# Now, when the manager updates the item of the day, a HTTP PATCH or PUT 
# call is sent to the API to set the status of the previous item of the day to Off. 
# Say item 16 is the item of the day, 
# the API for such a call would be menu-items/16 with an HTTP request body with a status set to Off. 
# The manager then manually selects a new item of the day, which makes another API call to update its status.


# A PUT or PATCH request is sent to menu-items/21 with a status parameter set to On in the HTTP request body. 
# The new item of the day is now item 21. 
# This way, there will be no chance of accidentally selecting the wrong menu item as the item of the day, 
# and you're keeping your API endpoints simple and focused.


# Filter, order, paginate:
# to filter large result sets and rearrange them in ascending or descending order. 

# Using pagination, 
# you can deliver results in smaller chunks. 
# For example, the API/menu-items returns all available menu items at once. 
# But a customer may want to see only the desserts or only the main courses, 
# so your API should be capable of filtering the results. 
# Previously, you've learned that you can accept 
# such filters as query string parameters to retrieve only appetizers or only mains. 
# When building an API, it is always a good idea to enable it to send results in smaller chunks. 

# This way, if the client application wants to display 20 menu items per page, 
# it will not need to make an API call for thousands of items all at once. 
# By using pagination, you can deliver API results in chunks, 
# and clients can decide the page number and how many records they want per page. 
# This API requests 4 items from page number 10, from a total page count of 16.
# /menu-items?perpage=4&page=10

# versioning:
# Did you know that you may break a client's applications 
# if you make changes to your API that might drastically change the response? 
# It's better to be safe and use versioning for your apps. 
# There are several factors to consider when deciding if an updated version is needed or 
# if a modification to an existing representation is enough. 

# In general, you should only support two versions of any given resource, 
# because maintaining multiple versions can be complex, error prone, and costly. 

# caching:
# API should be cacheable. 
# because it reduces the load on your database-related API calls. 
# You should always implement cacheing and send relevant HTTP headers in your response. 
# This will minimize the number of calls your client makes to your API. 

# For example, 
# if the mobile app makes a call to the endpoint menu-items, 
# you can cache the results the first time it runs, and then serve the cached result every time after that. 
# This way, you can avoid putting a heavy load on your database every time you need to fetch menu-items. 
# You will only update the cache when a menu item is modified or added. 

# For instance, if the appetizers menu was requested, 
# but if there are no modifications to the menu items, 
# all future calls to this endpoint can serve the same cached result without communicating with the database.
# And that saves a lot of computing power. 


# rate limiting 
# If you want to prevent abuse of your APIs, try rate limiting. 
# This limits the number of times someone can call your API in a period of time, like per minute, hour, or day. 
# Some people even limit their APIs per 30 days.


# monitoring:
# You should monitor latency to make sure your clients are getting the best possible response time. 
# If you are looking to get the most out of your API, it is essential to also monitor status codes. 
# By keeping an eye on 400 to 499 and 500 to 599 codes, 
# you can assure that your API runs smoothly and identify any potential problems early on. 
# Monitoring network bandwidth is also important to know if someone is abusing your API. 
# It's important to keep your API healthy, performant, and sustainable. 