from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def members1(request):
    return HttpResponse("Hello world!")


def members(request):
  template = loader.get_template('w3/myfirst.html')
  return HttpResponse(template.render())