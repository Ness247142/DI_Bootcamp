from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.PostIndex.as_view(), name='posts'),
    path('create_post/', views.PostCreateIndex.as_view(), name='create_post'),
]
