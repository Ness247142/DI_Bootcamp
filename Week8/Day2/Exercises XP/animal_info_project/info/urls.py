from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/animal/X', views.elon, name='animal')
    path('/family/X', views.elon, name='family')
]
