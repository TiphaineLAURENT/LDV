from django.db import models

# Create your models here.

class Vetements(models.Model):
    """
     Table représentant des vetements
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=50)
