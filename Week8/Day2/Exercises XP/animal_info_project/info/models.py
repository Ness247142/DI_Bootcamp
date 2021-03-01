from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=30, unique=True)

class Animal(models.Model):
    name = models.CharField(max_length=30, default='')
    legs = models.IntegerField(default=0)
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
