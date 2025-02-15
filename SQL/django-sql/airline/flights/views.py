from django.shortcuts import render, redirect
from django.http import Http404

from .models import *

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all(),
    })

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)  # get the flight whose id (primary key) is equal to flight_id
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),  # possible because passengers has a related_name="passengers"
        "non_passengers": Passenger.objects.exclude(flights=flight).all()  # passengers who are not on this flight
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)  # add the flight to the passenger's flights
        return redirect("flight", flight_id)


