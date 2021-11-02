from faker import Faker
from rent.models import Customer, Rental, Vehicle
import random


fake = Faker()

for i in range (15):
    rental = Rental()
    rental.rental_date = fake.date_between(start_date='-15d', end_date='today')
    print(rental.rental_date)
    rental.return_date = fake.date_between(start_date='-13d', end_date='today')
    rental.customer = Customer.objects.get(id=random.randint(1, 20))
    rental.vehicle = Vehicle.objects.get(id=i)
