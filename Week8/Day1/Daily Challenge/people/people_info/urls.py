from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='people'),
    path('about/', views.about, name='people_id'),
]