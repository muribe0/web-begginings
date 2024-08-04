from django.db import models

# Create your models here.
"""
class old_worse_Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
"""


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # on_delete = models.CASCADE -> if an airport is deleted, then all flights from or to that airport will also be
    # deleted. related_name = "departures" -> allows us to access all flights that have a particular airport as their

    # origin. so if I have an airport, I can access all flights that depart from that airport by calling
    # airport.departures.all()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

    def is_valid_flight(self):
        return self.origin != self.destination and self.duration > 0


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    # blank = True allows a Passanger to have no flights registered to them.
    # related_name = "passengers" allows us to access all passengers on a flight by calling flight.passengers.all()

    def __str__(self):
        return f"{self.first} {self.last}"