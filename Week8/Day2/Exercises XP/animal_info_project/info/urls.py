from django.urls import path
from . import views

urlpatterns = [
    path('family/<int:animal_id>', views.animal, name='family'),
    path('animal/<int:family_id>', views.family, name='animal'),
    path('animals/', views.animals, name='animals'),
]
