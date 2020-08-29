from django.shortcuts import render, get_object_or_404
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
    microcontrollers= Microcontroller.objects.order_by('-list_date').filter()
    context2 = {
        'microcontrollers': microcontrollers,
    }
    return render(request, 'products/product-view.html', context2)

# def microcontrollerid(request, microcontroller_id):
#     microcontrollerid= get_object_or_404(Microcontroller, pk= microcontroller_id)
#     # comments= ListComment.objects.filter(microcontroller = microcontroller)
#     context1= {
#         'microcontrollerid': microcontrollerid,
#         # 'comments': comments
#     }
#     return render(request, 'products/product-view.html', context1)

