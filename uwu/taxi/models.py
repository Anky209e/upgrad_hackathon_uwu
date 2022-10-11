from django.db import models
from traitlets import default

# Create your models here.
class Taxi(models.Model):
    date = models.DateTimeField()
    latitude=models.FloatField()
    longitude = models.FloatField()

