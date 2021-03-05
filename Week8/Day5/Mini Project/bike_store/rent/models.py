from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class VehicleType(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class VehicleSize(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.FloatField(default=0)
    size = models.CharField(max_length=50, default=0)

    def __repr__(self):
        return f"{self.vehicle_type} | {self.size}"

    def __str__(self):
        return f"{self.vehicle_type} | {self.size}"


class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return f"{self.rental_date}, {self.return_date}"

    def __str__(self):
        return f"{self.rental_date}, {self.return_date}"


class RentalRate(models.Model):
    daily_rate = models.FloatField(default=0)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, null=True)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return f"{self.vehicle_type} | {self.vehicle_size} | {self.daily_rate}"

    def __str__(self):
        return f"{self.vehicle_type} | {self.vehicle_size} | {self.daily_rate}"
