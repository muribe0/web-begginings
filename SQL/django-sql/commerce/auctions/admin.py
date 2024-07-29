from django.contrib import admin
from .models import *
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    filter_horizontal = ("wishlistedBy",)

admin.site.register(Listing, ListingAdmin)
admin.site.register(User) # This allows me to see it on the admin console
admin.site.register(Bid)