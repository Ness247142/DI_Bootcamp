from django.db import models
from django.utils.timezone import now


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f"Country: {self.name}"

    def __str__(self):
        return f"Country: {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f"Category: {self.name}"

    def __str__(self):
        return f"Category: {self.name}"


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __repr__(self):
        return f"Director: {self.first_name}, {self.last_name}"

    def __str__(self):
        return f"Director: {self.first_name}, {self.last_name}"


class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateTimeField(default=now, editable=True)
    created_in_country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True)
    available_in_country = models.ManyToManyField(
        Country, related_name='film_country')
    category = models.ManyToManyField(
        Category, related_name='film_category')
    director = models.ManyToManyField(
        Director, related_name='film_directory')

    def __repr__(self):
        return f"{self.title}",
        return f"Date: {self.release_date}"
        return f"Category: {self.category}"
        return f"Country: {self.created_in_country}"

    def __str__(self):
        return f"{self.title}",
        return f"Date: {self.release_date}"
        return f"Category: {self.category}"
        return f"Country: {self.created_in_country}"
