from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all(),
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id) # get me the flight whose id (primary key) is equal to flight_id
    return render(request, "flights/flight.html", {
        "flight": flight,
    })