from django.db import models
from django.utils import timezone

now = timezone.now()


class HotelVacancies(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class Bookings(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"
