from django.db import models


class Gif(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    uploader_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    likes = models.IntegerField()

    def __repr__(self):
        return f"{self.title}"

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    gifs = models.ManyToManyField(Gif, related_name='categories', blank=True)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"
