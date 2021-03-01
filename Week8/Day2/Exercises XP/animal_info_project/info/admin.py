from django.contrib import admin
from .models import Animal, Family  # import the Animal model


# Register your models here.
admin.site.register(Animal)
admin.site.register(Family)
