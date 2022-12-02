from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MedicationViewSet

router = DefaultRouter()
router.register("medication", MedicationViewSet, basename="medications")


urlpatterns = [
    path('', include(router.urls)),
]
