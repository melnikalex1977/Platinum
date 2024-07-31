from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    AstronomyShowViewSet,
    TicketViewSet,
    ShowThemeViewSet, ReservationViewSet,
)

router = routers.DefaultRouter()
router.register("astronomyshows", AstronomyShowViewSet)
router.register("ticket", TicketViewSet)
router.register("show_theme", ShowThemeViewSet)
router.register("reservation", ReservationViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "cinema"
