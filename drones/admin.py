from django.contrib import admin

from .models import Drone
from .models import DispatcherDrone
# Register your models here.

admin.site.register(Drone)
admin.site.register(DispatcherDrone)