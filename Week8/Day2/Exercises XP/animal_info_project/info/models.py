# import the models package. This line is already existing as soon as we use 'startapp'
from django.db import models

# Must inherit from Django Model class


class Animal(models.Model):
    legs = models.IntegerField(default=30)
    weight = models.CharField(max_length=40)
    height = models.CharField(max_length=40)
    speed = models.CharField(max_length=40)
    family = models.CharField(max_length=40)


class Family(models.Model):
    name = models.CharField(max_length=50)


def __repr__(self):
    return f"Animal {self.id}: {self.family}"


def __repr__(self):
    return f"Family {self.id}: {self.name}"
