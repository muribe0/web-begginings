from django.http import HttpResponse # This is a module that is used to return a response to the user
from django.shortcuts import render

# Create your views here.
def index(request):
#     return HttpResponse("Hello, worlddd!")
    return render(request, "hello/index.html") # This is a function that will render the index.html file

def greet(request, name):
#        return HttpResponse(f"Hello, {name.capitalize()}.")
    return render(request, "hello/greet.html", {
        "name": name.capitalize() # This is a dictionary that will be passed to the greet.html file
    }) # This is a function that will render the greet.html file