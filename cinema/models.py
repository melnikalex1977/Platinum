import os
from django.db import models
from django.conf import settings


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
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    row = models.IntegerField()
    seat = models.IntegerField()

    def __str__(self):
        return f"Ticket {self.id}"
