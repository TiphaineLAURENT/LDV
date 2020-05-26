from django.db import models
from django.core.files.images import ImageFile
from django.contrib.auth.models import AbstractUser
from django.conf import settings

import os

from polymorphic.models import PolymorphicModel


# Create your models here.

class User(AbstractUser):
    """
     Shopping user
    """


class Item(models.Model):
    """
     A inventory item
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="items")
    vetement = models.ForeignKey('Vetement', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vetement.name} for {self.user.username}"


class Vetement(PolymorphicModel):
    """
     Table représentant des vetements
    """

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(help_text="Une courte description")
    price = models.FloatField(default=50)

    def __str__(self):
        return self.name

    def description_trunc(self):
        return self.description[:3]

    class Meta:
        verbose_name = "Vetement"
        verbose_name_plural = "Vetements"


class Robe(Vetement):
    """
    """

    image = models.ImageField(default="/robe.jpg", upload_to="", blank=True)

    def save(self, *args, **kwargs):
        if not self.name.lower().startswith("robe"):
            self.name = f"Robe {self.name}"
        return super().save(*args, **kwargs)


class Pantalon(Vetement):
    """
    """

    image = models.ImageField(default="/pantalon.jpg", upload_to="", blank=True)

    def save(self, *args, **kwargs):
        if not self.name.lower().startswith("pantalon"):
            self.name = f"Pantalon {self.name}"
        if not self.image:
            self.image = self.image.field.default
        return super().save(*args, **kwargs)
