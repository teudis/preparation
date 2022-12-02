from django.db import models
from medications.models import Medication

# Create your models here.
# model (Lightweight, Middleweight, Cruiserweight, Heavyweight);
# state (IDLE, LOADING, LOADED, DELIVERING, DELIVERED, RETURNING).
class Drone(models.Model):
    DRONE_MODEL = (
        ("L", "Lightweight"),
        ("M", "Middleweight"),
        ("C", "Cruiserweight"),
        ("H", "Heavyweight"),
    )
    DRONE_STATE = (
        ("ID", "IDLE"),
        ("LO", "LOADING"),
        ("LD", "LOADED"),
        ("DE", "DELIVERING"),
        ("DD", "DELIVERED"),
        ("RE", "RETURNING"),
        
    )
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=1, choices=DRONE_MODEL)
    weigth_limit  = models.IntegerField()
    battery_capacity = models.IntegerField()
    state = models.CharField(max_length=2, choices=DRONE_STATE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    medications = models.ManyToManyField(Medication)
    
    def __str__(self):
        return self.serial_number
    
    

class DispatcherDrone(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    medications = models.ManyToManyField(Medication)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    total = models.FloatField(editable=False, blank=True, default=0)
    
    def __str__(self):
        return f"{self.drone.serial_number}--{str(self.created)}--{str(self.total)}"