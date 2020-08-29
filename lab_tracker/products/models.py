from django.db import models
from datetime import datetime

class Microcontroller(models.Model):
    title = models.CharField(max_length= 200)
    microcontroller= models.CharField(max_length=200)
    operating_voltage= models.IntegerField()
    input_voltage= models.CharField(max_length=200)
    input_voltage_limits= models.CharField(max_length=200)
    digital_inputOutput_pins = models.IntegerField()
    analog_pins = models.IntegerField()
    dc_current_per_inputOutput_pins = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', default= "blank")
    flash_memory = models.IntegerField()
    SRAM = models.IntegerField()
    clock_speed = models.IntegerField()
    typee = models.CharField(max_length=200)
    list_date = models.DateTimeField(default= datetime.now, blank= True)

    def __str__(self): 
        return self.title

    
class Motor(models.Model):
    title = models.CharField(max_length= 200)
    model= models.CharField(max_length=200)
    speed= models.CharField(max_length=200)
    voltage_range= models.CharField(max_length=200)
    typee= models.CharField(max_length=200)
    no_load_current = models.IntegerField()
    weight = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', default= "blank")
    list_date = models.DateTimeField(default= datetime.now, blank= True)

    def __str__(self):
        return self.title

class Led(models.Model):
    title = models.CharField(max_length= 200)
    led_size= models.IntegerField()
    wavelength= models.IntegerField()
    max_forward_current= models.IntegerField()
    waat= models.IntegerField()
    operating_temperature_range = models.CharField(max_length= 200)
    storage_temperature_range = models.CharField(max_length= 200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', default= "blank")
    list_date = models.DateTimeField(default= datetime.now, blank= True)

    def __str__(self):
        return self.title

class Sensor(models.Model):
    title= models.CharField(max_length= 200)
    operating_voltage_range = models.CharField(max_length= 200)
    level_output = models.CharField(max_length= 200)
    delay_time = models.CharField(max_length= 200)
    operation_temperature = models.CharField(max_length= 200)
    Range = models.CharField(max_length= 200)
    size = models.CharField(max_length= 200)
    pressure_range = models.CharField(max_length= 200, blank = True)
    temperature_accuracy = models.CharField(max_length= 200, blank = True) 
    diameter= models.CharField(max_length= 200, blank = True)
    length = models.CharField(max_length= 200, blank = True)
    switch_life_span = models.CharField(max_length= 200, blank = True)
    list_date = models.DateTimeField(default= datetime.now, blank= True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', default= "blank")
    
    def __str__(self):
        return self.title

class Wire(models.Model):
    title= models.CharField(max_length= 200)
    length = models.IntegerField()
    list_date = models.DateTimeField(default= datetime.now, blank= True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', default= "blank")

    def __str__(self):
        return self.title





    
