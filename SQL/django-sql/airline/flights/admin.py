from django.contrib import admin

from .models import *

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    # specify how the admin page should look like
    list_display = ("id", "origin", "destination", "duration")
    # This displays the id, origin, destination, and duration of each flight in the admin page as a TABLE

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",) # This allows us to filter passengers by flights


admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin) # The 2nd parameter tells the admin page how to display the Flight model
admin.site.register(Passenger, PassengerAdmin)