from django.urls import path
from . import views

#MAPPING BETWEEN ADDRESSES AND FUNCTIONS

urlpatterns = [
    path('', views.home, name='home'),
    path('mission/<int:id>', views.mission, name='mission'),
    path('elon/', views.elon, name='elon'),
    path('tesla/', views.tesla, name='tesla'),
    path('astros/', views.astronauts, name='astronauts'),
    path('add_astro/', views.add_astro, name='add-astronaut'),
]