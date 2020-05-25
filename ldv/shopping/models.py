from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
     Shopping user
    """
    vetements = models.ManyToManyField('Vetement')


class Item(models.Model):
    """
     A inventory item
    """


class Vetement(models.Model):
    """
     Table représentant des vetements
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=50)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    def description_trunc(self):
        return self.description[:3]

    class Meta:
        verbose_name = "Vetement"
        verbose_name_plural = "Vetements"
