from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Todo(models.Model):
    title = models.CharField(max_length=120)
    details = models.CharField(max_length=1000)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateField(auto_now_add=True)
    date_competion = models.DateField(null=True)
    deadline_date = models.DateField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()
    todo_list = models.ManyToManyField(Todo, blank=True)

    def __str__(self):
        return self.name
