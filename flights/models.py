from django.db import models
from django.core.validators import RegexValidator

only_alphabetic = RegexValidator(r"^[a-z, A-Z]*$", 'Only Alphabetic Characters (A-Z) Are Allowed.')

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3,validators=([only_alphabetic]))
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"

    def is_valid_flight(self):
        return self.origin != self.destination or self.duration >= 0


class Passenger(models.Model):
    First_Name = models.CharField(max_length=64)
    Last_Name = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
