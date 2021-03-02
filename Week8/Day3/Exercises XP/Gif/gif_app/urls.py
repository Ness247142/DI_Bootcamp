from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('gif_presentation/<int:gif_id>', views.gif_presentation, name='gif_presentation'),
]
