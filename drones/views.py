from rest_framework import generics

from .serializers import DroneSerializer, DroneBatterySerializer
from .models import Drone

# Create your views here.
class RegisteringDrone(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    
    
class AvalaibleDrone(generics.ListAPIView):
    serializer_class = DroneSerializer
    queryset = Drone.objects.filter(state="LO")
    

class CheckBatteryDrone(generics.RetrieveAPIView):
    serializer_class = DroneBatterySerializer
    queryset = Drone.objects.all()
    
