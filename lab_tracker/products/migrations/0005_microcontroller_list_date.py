# Generated by Django 3.0.3 on 2020-08-14 07:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_microcontroller_photo_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='microcontroller',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
