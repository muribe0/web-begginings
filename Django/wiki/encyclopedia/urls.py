from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:entry>/', views.visit_entry, name='loaded_entry'),
    path('random/', views.visit_random_entry, name='random_entry'),
    path('wiki/', views.search, name='search'),
    path('create/', views.create_entry, name='new_entry'),
    path('edit/<str:title>/', views.edit_entry, name='edit_entry')
]
