from django.db import models


class Astro(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=30)
    rank = models.CharField(max_length=20)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Mission(models.Model):
    name = models.CharField(max_length=50)
    pilot = models.ForeignKey(Astro, on_delete=models.CASCADE, null=True)
    launch_date = models.CharField(max_length=50, null=True)
    training_mission = models.BooleanField(default=False)

    # def __repr__(self):
    #     return f"Mission {self.id}: {self.name}"

    def get_pilot(self):
        return self.pilot or "No Pilot Selected Yet"
