from django.urls import path
from . import views

urlpatterns = [
    path('family/<int:families_id>', views.family, name='family'),
    path('animal/<int:animals_id>', views.animal, name='animal'),
]
