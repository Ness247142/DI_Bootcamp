from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('create/<str:userid>/', views.createTodo, name='create_todo_list'),
    path('todos/<str:userid>/', views.display_todos, name='display_to_do_list'),
]
