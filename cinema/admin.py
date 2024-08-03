from django.contrib import admin

from .models import (
    ShowTheme,
    AstronomyShow,
    PlanetariumDome,
    ShowSession,
    Ticket,
)

admin.site.register(ShowTheme)
admin.site.register(AstronomyShow)
admin.site.register(PlanetariumDome)
admin.site.register(ShowSession)
admin.site.register(Ticket)
