from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('add_film/', views.add_film, name='add_film'),
    path('add_director/', views.add_director, name='add_director'),
]
