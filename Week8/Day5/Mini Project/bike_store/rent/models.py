from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=30)


class VehicleType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class VehicleSize(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    real_cost = models.IntegerField()
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)


class Rental(models.Model):
    rental_date = models.DateField(max_length=50)
    return_date = models.DateField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class RentalRate(models.Model):
    daily_rate = models.SmallIntegerField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
