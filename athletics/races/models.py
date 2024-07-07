from django.db import models
from django.utils import timezone


class Race(models.Model):
    name = models.CharField(max_length=100)
    event_start = models.DateTimeField()

    def __str__(self):
        return self.name


class Athlete(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()  # Add this field if it doesn't exist email_sent_to_athlete

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class RaceResult(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    position = models.IntegerField()

    def __str__(self):
        return f'{self.athlete} - {self.race} - {self.position}'

