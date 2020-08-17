from django.contrib import admin
from .models import Microcontroller, Motor, Led,Sensor, Wire

admin.site.register(Microcontroller)
admin.site.register(Motor)
admin.site.register(Led) 
admin.site.register(Sensor)
admin.site.register(Wire)