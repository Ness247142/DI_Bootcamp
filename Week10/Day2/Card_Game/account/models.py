from django.db import models
from django.contrib.auth.models import User

SPECIES = (
    ('jedi', 'JEDI'),
    ('hutt', 'HUTT'),
    ('wookie', 'WOOKIE'),
    ('sith', 'SITH')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.URLField(max_length=254, default='https://www.elegantthemes.com/blog/wp-content/uploads/2020/02/000-404.png')
    species = models.CharField(max_length=20, choices=SPECIES, default='jedi')
    number_of_points = models.IntegerField(default=0)

    def __str__(self):
        if self.user:
            return self.user.username
        return self.number_of_points