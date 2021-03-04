from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rent/rental/', views.rental, name='rental'),
    path('rent/rental/<int:id>', views.rental_id, name='rental_id'),
    path('rent/rental/add', views.rental_add, name='rental_add'),
    path('rent/customer/<int:id>', views.customer_id, name='customer_id'),
    path('rent/customer/', views.customer, name='customer'),
    path('rent/customer/add', views.customer_add, name='customer_add'),
    path('rent/vehicle/', views.vehicle, name='vehicle'),
    path('rent/vehicle/<int:id>', views.vehicle_id, name='vehicle_id'),
    path('rent/vehicle/add', views.vehicle_add, name='vehicle_add'),
]
