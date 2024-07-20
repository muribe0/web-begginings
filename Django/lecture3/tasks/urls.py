from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"), # This is a path that will be used to access the index function in the views.py file
    path("add", views.add, name="add"),
]