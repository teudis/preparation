from rest_framework import viewsets
from .serializer import MedicationSerializer
from .models import Medication

# Create your views here.
class MedicationViewSet(viewsets.ModelViewSet):
    serializer_class = MedicationSerializer
    queryset = Medication.objects.all()