from rent.models import VehicleType, VehicleSize, Vehicle, Rental, RentalRate, Customer
import random
from faker import Faker
fake = Faker()

def populate_rental_rates():
    if RentalRate.objects.all().count() != 24:
        sizes = VehicleSize.objects.all()
        types = VehicleType.objects.all()

        for type in types:
            for size in sizes:
                rental, created = RentalRate.objects.get_or_create(vehicle_type=type, vehicle_size=size, daily_rate=random.randint(15, 100))

                
def populate_vehicles(number):
    sizes = VehicleSize.objects.all()
    types = VehicleType.objects.all()
    for i in range(number):
        Vehicle.objects.create(real_cost=random.randint(100, 800),size=random.choice(sizes), vehicle_type=random.choice(types))


def populate_rentals(number):
    customers = Customer.objects.all()
    vehicles = Vehicle.objects.all()
    for i in range(number):
        Rental.objects.create(customer=customers[i], vehicle=vehicles[i], rental_date=fake.date_time_between(start_date='-10d', end_date='-4d'), return_date=fake.date_time_between(start_date='-3d', end_date='-1d'))
