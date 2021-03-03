from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=30)
    details = models.CharField(max_length=30)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"{self.title}: {self.details}"

    def __str__(self):
        return f"({self.id}) {self.title}"


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField(max_length=200)
    todo = models.ManyToManyField(Todo, related_name="all_todos")

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"({self.id}): {self.name}"
