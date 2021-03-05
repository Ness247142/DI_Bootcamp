from faker import Faker

from .models import *


fake = Faker()


def populateCustomer(num):
    for numb in range(num):
        Customer.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            address=fake.address(),
            city=fake.city(),
            country=fake.country(),
        )
