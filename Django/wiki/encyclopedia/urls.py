from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:entry>/', views.visit_entry, name='loaded_entry'),
    path('random/', views.visit_random_entry, name='random_entry'),
    path('wiki/', views.search, name='search'),
]
