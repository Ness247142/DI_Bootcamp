from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rental/', views.rental, name='rental'),
    path('rental/<int:pk>', views.rental_id, name='rental_id'),
    path('rental/add/', views.rental_add, name='rental_add'),
    path('customer/<int:pk>', views.customer_id, name='customer_id'),
    path('customer/', views.customer, name='customer'),
    path('customer/add/', views.customer_add, name='customer_add'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('vehicle/<int:pk>', views.vehicle_id, name='vehicle_id'),
    path('vehicle/add/', views.vehicle_add, name='vehicle_add'),
]
