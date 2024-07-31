from django.contrib import admin

from .models import (
    ShowTheme,
    AstronomyShow,
    Ticket,
    Reservation,
)

admin.site.register(ShowTheme)
admin.site.register(AstronomyShow)
admin.site.register(Ticket)
admin.site.register(Reservation)
