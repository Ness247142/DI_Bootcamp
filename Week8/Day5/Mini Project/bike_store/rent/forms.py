from django import forms


class AddVehicleForm(forms.Form):
    vehicle_type = forms.CharField(required=True)
    vehicle_size = forms.FloatField(required=True)


class AddCustomerForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField()
    phone_number = forms.CharField(required=True)


class AddRentalForm(forms.Form):
    customer_id = forms.IntegerField(required=True)
    vehicle_id = forms.IntegerField(required=True)
