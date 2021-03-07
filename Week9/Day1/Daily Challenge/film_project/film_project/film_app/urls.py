from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add_film/', views.add_film, name='add_film'),
    path('add_director/', views.AddDirector.as_view(), name='add_director'),
]
