from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    content="<html><body><h1>Welcome little lemon</h1></body></html>"
    return HttpResponse(content)