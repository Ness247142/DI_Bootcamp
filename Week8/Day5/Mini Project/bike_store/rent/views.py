from django.shortcuts import render, redirect
from .models import Customer, VehicleType, VehicleSize, Vehicle, Rental, RentalRate
from .forms import AddCustomerForm, AddRentalForm, AddVehicleForm

# Create your views here.

def index(request):
    context = {
        'title': "Home Page",
        'heading': "Home Page",
        'summary': "This page will have links to different pages and some nice pictures or whatever.",
    }
    return render(request, "index.html", context)

# SECTION 1: RENTALS


def rentals(request):
    context = {
        'title': "Rentals Page",
        'heading': "Rentals Page",
        'summary': "This page should show a list of all rentals, unreturned first, then ordered by date ascending (earliest first)",
        'rentals': Rental.objects.all(),
    }
    return render(request, "rentals.html", context)


def rental_details(request, rental_id):
    this_rental = Rental.objects.get(id=rental_id)
    context = {
        'title': "Rental Details Page",
        'heading': "Rental Details Page",
        'summary': "This page should show the information about the given rental based on ID in URL",
        'rental': this_rental,
    }
    return render(request, "rental_details.html", context)


def add_rental(request):
    context = {
        'title': "Add Rental Page",
        'heading': "Add Rental Page",
        'summary': "This page should display a form of some kind to add a rental",
        'form': AddRentalForm(),
    }
    if request.method == 'POST':
        form = AddRentalForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'add_rental.html', context)

# SECTION 2: RENTALS


def customers(request):
    context = {
        'title': "Customers Page",
        'heading': "Customers Page",
        'summary': "This page should show a list of all customers, ideally in alphabetical order, linking to customer details page",
        'customers': Customer.objects.all(),
    }
    return render(request, "customers.html", context)


def customer_details(request, customer_id):
    this_customer = Customer.objects.get(id=customer_id)
    context = {
        'title': "Customer Details Page",
        'heading': "Customer Details Page",
        'summary': "This page should show the information about the given Customer based on ID in URL",
        'customer': this_customer,
    }
    return render(request, "customer_details.html", context)


def add_customer(request):
    context = {
        'title': "Add Customer Page",
        'heading': "Add Customer Page",
        'summary': "This page should display a form of some kind to add a Customer",
        'form': AddCustomerForm(),
    }
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'add_customer.html', context)


# SECTION 3: VEHICLES
def vehicles(request):
    context = {
        'title': "Vehicles Page",
        'heading': "Vehicles Page",
        'summary': "This page should show a list of all vehicles, ideally in a sensible order, linking to vehicle details page",
        'vehicles': Vehicle.objects.all(),
    }
    return render(request, "vehicles.html", context)


def vehicle_details(request, vehicle_id):
    this_vehicle = Vehicle.objects.get(id=vehicle_id)
    context = {
        'title': "Vehicle Details Page",
        'heading': "Vehicle Details Page",
        'summary': "This page should show the information about the given Vehicle based on ID in URL",
        'vehicle': this_vehicle,
    }
    return render(request, "vehicle_details.html", context)


def add_vehicle(request):
    context = {
        'title': "Add Vehicle Page",
        'heading': "Add Vehicle Page",
        'summary': "This page should display a form of some kind to add a Vehicle",
        'form': AddVehicleForm(),
    }
    if request.method == 'POST':
        form = AddVehicleForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'add_vehicle.html', context)
