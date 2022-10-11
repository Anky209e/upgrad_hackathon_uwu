from django.db import models


# Create your models here.

class fakenews(models.Model):
    news = models.TextField()