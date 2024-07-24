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
