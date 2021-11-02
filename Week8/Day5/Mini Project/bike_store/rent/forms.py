from django import forms
from django.forms import Form, ModelForm
from .models import Customer, VehicleType, VehicleSize, Vehicle, Rental, RentalRate

class AddRentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = "__all__"


class AddCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class AddVehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"
