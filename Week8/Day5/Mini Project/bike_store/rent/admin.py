from django.contrib import admin
from .models import *

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'size', 'date_created')
admin.site.register(Vehicle, VehicleAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'phone_number', 'address', 'city', 'country')
admin.site.register(Customer, CustomerAdmin)


class RentalAdmin(admin.ModelAdmin):
    list_display = ('customer', 'vehicle', 'rental_date', 'return_date')
admin.site.register(Rental, RentalAdmin)

admin.site.register(VehicleType)
admin.site.register(VehicleSize)
admin.site.register(RentalRate)
