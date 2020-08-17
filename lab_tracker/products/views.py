from django.shortcuts import render
from .models import Microcontroller, Motor, Led, Sensor, Wire


def product(request):
    microcontrollers= Microcontroller.objects.order_by('-list_date').filter()
    motors= Motor.objects.order_by('-list_date').filter()
    leds= Led.objects.order_by('-list_date').filter()
    sensor= Sensor.objects.order_by('-list_date').filter()
    wires= Wire.objects.order_by('-list_date').filter()

    context= {
        'microcontrollers': microcontrollers,
        'motors': motors,
        'leds': leds,
        'sensors': sensor,
        'wires': wires,
        
    }
    return render(request, 'products/products.html', context)

def productview(request):
    return render(request, 'products/product-view.html')
