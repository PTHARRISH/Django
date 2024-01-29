# Introduction
# In this exercise, you are going to use the REST API client Insomnia to make HTTP Requests 
# so make sure you’ve installed it on your computer. You will also use the Request and Response Service httpbin.org. 
# Httpbin.org is an open-source web service that allows you to make HTTP calls without any additional installations or dependencies. 

# You will be exploring the different functionalities available in Insomnia such as:

# Creating a GET request
# Creating a POST request with Form Data
# Creating a POST request with JSON Data

# Instructions
#  To get started, open Insomnia on your local device and navigate to the tab labeled DEBUG.    

# The DEBUG tab in Insomnia
#  If you haven't installed Insomnia yet, you can download the install files at 
# https://insomnia.rest/
   

# Create a GET request
# Open the https://httpbin.org/ website and click on HTTP Methods. 
# A menu with different HTTP methods will expand which you can add to your endpoints.
# Menu ITEM The HTTP Methods menu on the httpbin.org website includes options such as DELETE, GET, PATCH and POST.

# Step 1:
# In Insomnia, click on the + icon on the left-hand side of the screen and select HTTP Request from the drop-down menu.
# The + icon in Insomnia provides access to a menu of different requests including HTTP Request.

# Step 2:
# Double-click the request to change its title to GET request using Insomnia. 

# Step 3: 
# Click on the GET dropdown to see a list of available options and re-select GET. 

# Update the URL endpoint with the value: 
# https://httpbin.org/get
# Press the Send button and notice the JSON output. 

# output:
# {
# 	"args": {},
# 	"headers": {
# 		"Accept": "*/*",
# 		"Host": "httpbin.org",
# 		"User-Agent": "insomnia/8.5.1",
# 		"X-Amzn-Trace-Id": "Root=1-659e4e6d-38ee006d55401f894e637e83"
# 	},
# 	"origin": "152.58.232.211",
# 	"url": "https://httpbin.org/get"
# }


# Step 4:
# From the Body drop-down option, select Multipart Form. 
# Add the following values under New name and New value:
# New name: title
# New value: Lord of the Rings

#  Press the Send button once again and observe the changes.  
# Notice that the value of Content-Length has been updated to include the changes.

# output:
# {
# 	"args": {},
# 	"headers": {
# 		"Accept": "*/*",
# 		"Content-Length": "111",
# 		"Content-Type": "multipart/form-data; boundary=X-INSOMNIA-BOUNDARY",
# 		"Host": "httpbin.org",
# 		"User-Agent": "insomnia/8.5.1",
# 		"X-Amzn-Trace-Id": "Root=1-659e4f29-2883dc4f19151de71d1eaff7"
# 	},
# 	"origin": "152.58.232.211",
# 	"url": "https://httpbin.org/get"
# }


# Step 5: 
# Update a form entry with the following details:

# New name: author
# New value: JRR Tolkien            

# Press the Send button once again. Notice that Content-Length has further been updated. 

# output:
# {
# 	"args": {},
# 	"headers": {
# 		"Accept": "*/*",
# 		"Content-Length": "196",
# 		"Content-Type": "multipart/form-data; boundary=X-INSOMNIA-BOUNDARY",
# 		"Host": "httpbin.org",
# 		"User-Agent": "insomnia/8.5.1",
# 		"X-Amzn-Trace-Id": "Root=1-659e4fa8-096db2aa441f88747dd99ae3"
# 	},
# 	"origin": "152.58.232.55",
# 	"url": "https://httpbin.org/get"
# }


# Step 6: 
# You can Filter your output using the Filter response body at the section in the bottom right-hand side of Insomnia 
# as indicated in the screenshot below. 

# Filter functionality in Insomnia
# Add the following filter inside it:

# $.origin
# It should update the Preview. 
# The output will appear similar to what is displayed in the screenshot below.

# output:
# [
# 	"152.58.232.55"
# ]

# Output when using the $.origin filter in Insomnia

# Step 7: 
# Modify the filter incrementally as below which should produce the respective outputs.

# $.headers

# output:
# [
# 	{
# 		"Accept": "*/*",
# 		"Content-Length": "196",
# 		"Content-Type": "multipart/form-data; boundary=X-INSOMNIA-BOUNDARY",
# 		"Host": "httpbin.org",
# 		"User-Agent": "insomnia/8.5.1",
# 		"X-Amzn-Trace-Id": "Root=1-659e4fa8-096db2aa441f88747dd99ae3"
# 	}
# ]

# Output when using the  $.headers filter in Insomnia.

# $.headers.Content-Type

# output:
# [
# 	"multipart/form-data; boundary=X-INSOMNIA-BOUNDARY"
# ]

# Output using the  $.headers.Content-Type filter in Insomia
# Note: The dot operator is used here to explore the contents of the JSON output. Also notice the value of the Content-Type is form-data because you selected Multipart form. 
# Clear the contents of the Filter response body. 


# Step 8:
# Now deselect the option for the name title and re-create the GET request.

# output:
# {
# 	"args": {},
# 	"headers": {
# 		"Accept": "*/*",
# 		"Content-Length": "110",
# 		"Content-Type": "multipart/form-data; boundary=X-INSOMNIA-BOUNDARY",
# 		"Host": "httpbin.org",
# 		"User-Agent": "insomnia/8.5.1",
# 		"X-Amzn-Trace-Id": "Root=1-659e513a-7fac8e934c210ad200e7f639"
# 	},
# 	"origin": "152.58.232.55",
# 	"url": "https://httpbin.org/get"
# }
                                         

# Notice the change in the Content-Length again.

# Additional step

# Now that you know the steps to create a GET request in Insomnia, 
# you can explore different configuration settings by following the steps discussed to get more accustomed to the tool.


# Create a POST request with Form Data

#  Step 1:
# Keeping the contents of the form data the same, update the request type to POST and update the URL endpoint to:

# https://httpbin.org/post

# POST request selected from drop-down menu in Insomnia.
# Press the Send button again. The output should appear as below:
# Form data output of a POST request in Insomnia
# Notice that the contents of the form are updated inside the output for the POST request. 

# output:
# {
# 	"args": {},
# 	"data": "",
# 	"files": {},
# 	"form": {
# 		"author": "jrr tolkien",
# 		"title": "lord of the rings"
# 	},
# 	"headers": {
# 		"Accept": "*/*",
# 		"Content-Length": "200",
# 		"Content-Type": "multipart/form-data; boundary=X-INSOMNIA-BOUNDARY",
# 		"Host": "httpbin.org",
# 		"User-Agent": "insomnia/8.5.1",
# 		"X-Amzn-Trace-Id": "Root=1-659e51c9-5d3f5f131b0d4cbd02fff909"
# 	},
# 	"json": null,
# 	"origin": "152.58.232.55",
# 	"url": "https://httpbin.org/post"
# }


# Step 2:
# Explore the other tabs under the output such as Headers, Cookies and Timeline.
# Tabs in the output section of Insomnia like Headers, Cookies and Timeline


# Step 3:      
# Since you have modified the same HTTP request, update the changes for the 
# title of the request in the left-hand section to POST request using Insomnia.

# New title of the POST request in Insomnia


# Create a POST request with JSON Data
#  Step 1:
# Now further create another HTTP Request like the one at the beginning by 
# pressing the + icon and selecting HTTP Request. 

# Step 2:
# Update the request type to POST and the request label as:

# POST request using JSON object
# Note: The labels are for reference and independent of the request type.

# Paste the same URL endpoint that you used earlier in the URL text-box:
# https://httpbin.org/post
# The updated view should appear as below:
# Insomnia with two POST requests appearing in the left-hand pane

# Step 3:
# Under the Body dropdown option, select JSON as the text input.
# JSON is an option under the text input section in the dropdown menu of the Body option.
# A text input area should appear as below.

# A text input area that appears after selecting JSON as the text input in Insomnia
# Step 4:
# Enter the following content inside the text input area:

# {
#             "title": "Lord of the Rings",
#             "author": "JRR Tolkien",
#             "published" : {
#                         "year": 1954,
#                         "month": "july",
#                         "day" : 29
#             }
# }

#  Press the Send button. 

# output:
# {
# 	"args": {},
# 	"data": "{\n            \"title\": \"Lord of the Rings\",\n            \"author\": \"JRR Tolkien\",\n            \"published\" : {\n                        \"year\": 1954,\n                        \"month\": \"july\",\n                        \"day\" : 29\n            }\n}\n",
# 	"files": {},
# 	"form": {},
# 	"headers": {
# 		"Accept": "*/*",
# 		"Content-Length": "239",
# 		"Content-Type": "application/json",
# 		"Host": "httpbin.org",
# 		"User-Agent": "insomnia/8.5.1",
# 		"X-Amzn-Trace-Id": "Root=1-659e52ed-2cf8b3db3bc0a6416f25768a"
# 	},
# 	"json": {
# 		"author": "JRR Tolkien",
# 		"published": {
# 			"day": 29,
# 			"month": "july",
# 			"year": 1954
# 		},
# 		"title": "Lord of the Rings"
# 	},
# 	"origin": "152.58.232.55",
# 	"url": "https://httpbin.org/post"
# }

#  The output for the JSON input should appear as below: 

# Output of a POST request with JSON set as the text input.
# Notice the contents entered as JSON object in both the data and json field inside the JSON output. 

# Step 5:
# Add the following line to Filter response body:

# $.json.published.year

#  The output will be as follows:

# 
# [
# 	1954
# ]

# Modify the Filter response body as follow:

#  $[json][published][day]

#  The output will be as follows:

# [
# 	29
# ]

# Concluding Thoughts
# There are several configuration options inside Insomnia. While using a REST API client it is good to explore these. 
# You can also get help from other free and open-source API services that provide options to make API calls to access public data. 


