# Generated by Django 3.0.8 on 2020-08-17 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_wire'),
    ]

    operations = [
        migrations.AddField(
            model_name='wire',
            name='photo_main',
            field=models.ImageField(default='blank', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
