import os
import pathlib
import uuid

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class ShowTheme(models.Model):
    name = models.CharField(max_length=255)


def product_image_file_path(instance: "AstronomyShow", filename: str) -> str:
    filename = (
        f"{instance.title} - {instance}"
    )
    return os.path.join(settings.MEDIA_ROOT, filename)

class AstronomyShow(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    show_theme = models.ManyToManyField(ShowTheme, related_name="astronomy_shows")
    image = models.ImageField(null=True, upload_to="product_image_file_path")


    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField(default=0)
    seats_in_row = models.IntegerField(default=0)

class ShowSession(models.Model):
    show_time = models.DateTimeField()
    astronomy_show = models.ForeignKey(AstronomyShow, on_delete=models.CASCADE)
    planetarium_dome = models.ForeignKey(PlanetariumDome, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ["-show_time"]


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations"
    )

    def __str__(self) -> str:
        return str(self.created_at)


class Ticket(models.Model):
    show_session = models.ForeignKey(
        ShowSession, on_delete=models.CASCADE, related_name="tickets"
    )
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    row = models.IntegerField()
    seat = models.IntegerField()

    def __str__(self):
        return f"Ticket {self.id} for {self.show_session}"
