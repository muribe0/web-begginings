from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Listing)
admin.site.register(User) # This allows me to see it on the admin console