from django.db import models


class Astro(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=30)
    rank = models.CharField(max_length=20)
    likes = models.IntegerField(default=0)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Astronaut: ID: {self.id}: {self.first_name} {self.last_name}"


class MedProfile(models.Model):
    astro = models.OneToOneField(Astro, on_delete=models.CASCADE, primary_key=True)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    clearance = models.BooleanField(default=True)

    def __repr__(self):
        return f"Medical Profile for {self.astro}"


class Mission(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    pilot = models.ForeignKey(Astro, on_delete=models.SET_NULL, null=True)
    launch_date = models.CharField(max_length=50, null=True)
    training_mission = models.BooleanField(default=False)

    def __repr__(self):
        return f"Mission {self.id}: {self.name}"

    def __str__(self):
        return f"Mission {self.id}: {self.name}"

    def get_pilot(self):
        return self.pilot or "No Pilot Selected Yet"


class Rocket(models.Model):
    name = models.CharField(max_length=50)
    fuel_capacity = models.IntegerField(default=0)
    max_weight = models.IntegerField(default=0)
    thrust = models.IntegerField(default=0)
    image = models.URLField(max_length=200)
    missions = models.ManyToManyField(Mission, related_name="all_rockets")


    def __repr__(self):
        return f"Rocket: {self.name}"

    def __str__(self):
        return f"Rocket: {self.name}"
