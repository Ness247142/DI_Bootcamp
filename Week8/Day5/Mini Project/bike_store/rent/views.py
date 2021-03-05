from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.http import Http404
from .forms import *


def home(request):
    return render(request, 'home.html')


def rental(request):
    my_rental = Rental.objects.all()
    context = {
        'my_rental': my_rental
    }
    return render(request, 'rental.html', context)


def rental_id(request, pk):
    return render(request, 'rental_id.html', {'rental_id': Rental.objects.get(id=rental_id)})


def rental_add(request):
    if request.method == "GET":
        myform = AddRentalForm()
        return render(request, 'rental_add.html', {'myform': myform})

    if request.method == "POST":

        myform = AddRentalForm(request.POST)

        if myform.is_valid():
            customer_id = myform.cleaned_data['customer_id']
            vehicle_id = myform.cleaned_data['vehicle_id']

            a1 = Rental(customer_id=customer_id,
                        vehicle_id=vehicle_id)
            a1.save()

            return redirect('rental')

        else:
            return render(request, 'rental_add.html', {'myform': myform})


def customer_id(request, pk):
    return render(request, 'customer_id.html', {'customer_id': Customer.objects.get(id=customer_id)})


def customer(request):
    my_customer = Customer.objects.all().order_by('last_name')
    context = {
        'my_customer': my_customer
    }
    return render(request, 'customer.html', context)


def customer_add(request):
    if request.method == "GET":
        myform = AddCustomerForm()
        return render(request, 'customer_add.html', {'myform': myform})

    if request.method == "POST":

        myform = AddCustomerForm(request.POST)

        if myform.is_valid():
            first_name = myform.cleaned_data['first_name']
            last_name = myform.cleaned_data['last_name']
            email = myform.cleaned_data['email']
            phone_number = myform.cleaned_data['phone_number']
            address = myform.cleaned_data['address']
            city = myform.cleaned_data['city']
            country = myform.cleaned_data['country']

            a1 = Customer(first_name=first_name,
                          last_name=last_name, email=email, phone_number=phone_number, address=address, city=city, country=country)
            a1.save()

            return redirect('customer')

        else:
            return render(request, 'customer_add.html', {'myform': myform})


def vehicle(request):
    my_vehicle = Vehicle_type.objects.all()
    context = {
        'my_vehicle': my_vehicle
    }
    return render(request, 'vehicle.html', context)


def vehicle_id(request, pk):
    return render(request, 'vehicle_id.html', {'vehicle_id': Vehicle.objects.get(id=vehicle_id)})


def vehicle_add(request):
    if request.method == "GET":
        myform = AddVehicleForm()
        return render(request, 'vehicle_add.html', {'myform': myform})

    if request.method == "POST":

        myform = AddVehicleForm(request.POST)

        if myform.is_valid():
            vehicle_type = myform.cleaned_data['vehicle_type']
            vehicle_size = myform.cleaned_data['vehicle_size']

            a1 = Vehicle(vehicle_type=vehicle_type,
                         vehicle_size=vehicle_size,)
            a1.save()

            return redirect('vehicle')

        else:
            return render(request, 'vehicle_add.html', {'myform': myform})
