from django.db import models
from datetime import datetime
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    released_date = models.DateField(default=datetime.now())

    def get_absolute_url(self):
        return reverse('posts')

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f"{self.title}"
