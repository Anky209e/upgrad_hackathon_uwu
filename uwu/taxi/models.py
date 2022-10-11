from django.db import models
from traitlets import default

# Create your models here.
class Taxi(models.Model):
    date = models.DateField()
    time = models.TimeField()
    latitude=models.FloatField()
    longitude = models.FloatField()

