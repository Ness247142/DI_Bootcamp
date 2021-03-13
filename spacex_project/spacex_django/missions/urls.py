from django.urls import path
from . import views

#MAPPING BETWEEN ADDRESSES AND FUNCTIONS

urlpatterns = [
    path('', views.home, name='home'),
    path('mission/<int:id>', views.mission, name='mission'),
    path('elon/', views.elon, name='elon'),
    path('tesla/', views.tesla, name='tesla'),
    path('astros/', views.astronauts, name='astronauts'),
    path('astros/like/', views.like_astro, name='like-astro'),
    path('add_astro/', views.add_astro, name='add-astronaut'),
    path('add_mission/', views.add_mission, name='add-mission'),
    path('see_rockets/', views.AllRockets.as_view(), name='see-rockets'),
    path('rocket_details/<int:pk>', views.RocketDeets.as_view(), name='rocket-details'),
    path('add_rocket/', views.AddRocket.as_view(), name='add-rocket'),

    # path('custom_login', views.custom_login, name='custom-login')  #If we build Login ourselves
]