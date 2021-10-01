from django.urls import path
from . import views

urlpatterns = [
    path('', views.phone_app, name='phone_app'),
]

