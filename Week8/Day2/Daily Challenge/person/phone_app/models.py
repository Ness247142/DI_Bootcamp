from django.db import models
from datetime import date



class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_number = models.PhoneNumberField()
    address = models.CharField(max_length=50)