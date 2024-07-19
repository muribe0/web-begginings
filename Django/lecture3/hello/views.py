from django.http import HttpResponse # This is a module that is used to return a response to the user
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, worlddd!")

def greet(request, name):
       return HttpResponse(f"Hello, {name.capitalize()}.")