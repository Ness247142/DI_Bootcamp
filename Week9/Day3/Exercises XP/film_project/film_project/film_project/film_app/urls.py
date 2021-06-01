from django.contrib import admin
from django.urls import path, include
from . import views
from .views import AddDirector, Profile, FilmUpdate, DirectorUpdate

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/<pk>', Profile.as_view(), name='profile'),
    path('add_film/', views.add_film, name='add_film'),
    path('update_film/<int:pk>', FilmUpdate.as_view(), name='update_film'),
    path('update_director/<int:pk>',
         DirectorUpdate.as_view(), name='update_director'),
    path('add_director/', AddDirector.as_view(), name='add_director'),
]
