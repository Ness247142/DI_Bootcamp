from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/animal/X', views.elon, name='home-animal')
    path('/family/X', views.elon, name='home-family')
]