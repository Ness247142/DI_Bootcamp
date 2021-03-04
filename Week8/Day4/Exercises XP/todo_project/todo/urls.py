from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/', views.todo, name='todo'),
    path('display_todos/', views.display_todos, name='display_todos'),
]
