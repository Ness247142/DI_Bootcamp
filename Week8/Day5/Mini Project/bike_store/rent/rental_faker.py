from faker import Faker

from .models import *

import random


fake = Faker()


def populateRental(num):
    for numb in range(num):
        Rental.objects.create(
            rental_date=fake.date(),
            return_date=fake.date(),
            customer=fake.name(0, 100),
            vehicle=random.randint(1, 5)
        )
