from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("", views.index, name="index"),
    path("rentals", views.rentals, name="rentals"),
    path("rentals/details/<rental_id>",
         views.rental_details, name="rental_details"),
    path("rentals/add", views.add_rental, name="add_rental"),
    path("customers", views.customers, name="customers"),
    path("customers/details/<customer_id>",
         views.customer_details, name="customer_details"),
    path("customers/add", views.add_customer, name="add_customer"),
    path("vehicles", views.vehicles, name="vehicles"),
    path("vehicles/details/<vehicle_id>",
         views.vehicle_details, name="vehicle_details"),
    path("vehicles/add", views.add_vehicle, name="add_vehicle"),
]
