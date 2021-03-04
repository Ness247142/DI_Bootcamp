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
    name = models.CharField(max_length=50)

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
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created = models.CharField(max_length=50, null=True)
    real_cost = models.FloatField(default=0)
    size = models.CharField(max_length=50, default=0)

    def __repr__(self):
        return f"{self.vehicle_type} {self.date_created}"

    def __str__(self):
        return f"{self.vehicle_type}, {self.date_created}"


class Rental(models.Model):
    rental_date = models.CharField(max_length=50, null=True)
    return_date = models.CharField(max_length=50, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.rental_date}, {self.return_date}"

    def __str__(self):
        return f"{self.rental_date}, {self.return_date}"


class RentalRate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.daily_rate}"

    def __str__(self):
        return f"{self.daily_rate}"
