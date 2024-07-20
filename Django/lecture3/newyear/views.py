from django.shortcuts import render
from datetime import datetime



# Create your views here.
def index(request):
    now = datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1 # This will return True if the current month is January and the current day is the first day of the month
    })