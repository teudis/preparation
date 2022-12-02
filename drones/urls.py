from django.urls import path

from .views import RegisteringDrone, AvalaibleDrone, CheckBatteryDrone

urlpatterns = [
    path("list",RegisteringDrone.as_view(),name="list-drones"),
    path("available", AvalaibleDrone.as_view(), name="available-drones"),
    path("battery/<int:pk>", CheckBatteryDrone.as_view(), name="check-battery"),
]