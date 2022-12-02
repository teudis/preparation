from rest_framework import serializers
from medications.serializer import MedicationSerializer

from .models import Drone

class DroneSerializer(serializers.ModelSerializer):
    medications = MedicationSerializer(read_only=True, many=True)
    
    class Meta:
        model = Drone
        fields = "__all__"
        
        

class DroneBatterySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Drone
        fields = ["id","serial_number","battery_capacity","state"]
        