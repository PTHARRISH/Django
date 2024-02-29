from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from datetime import datetime
# Create your views here.

def home(request):
    content="<html><body><h1>Welcome little lemon</h1></body></html>"
    return HttpResponse(content)

def say_hello(request):
    return HttpResponse("Hello world")

def homepage(request):
    return HttpResponse("Welcome to Little Lemon!")

def display_date(request):
    date_joined=datetime.today().year
    return HttpResponse(date_joined)


# def myview(request): 
#     if request.method=='GET': 
#         val = request.GET['key'] 
#         #perform read or delete operation on the model 
#     if request.method=='POST': 
#         val = request.POST['key'] 
#         #perform insert or update operation on the model 

#     if request.method=='POST':  
#         #perform insert or update operation on the model  
#         context={ } #dict containing data to be sent to the client  

#     return render(request, 'mytemplate.html', context) 

# class MyView(View): 
#     def get(self, request): 
#         # logic to process GET request
#         return HttpResponse('response to GET request') 
 
#     def post(self, request): 
#         # <logic to process POST request> 
#         return HttpResponse('response to POST request') 