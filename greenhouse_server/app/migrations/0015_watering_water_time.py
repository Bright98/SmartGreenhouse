# Generated by Django 3.0.7 on 2020-07-22 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20200722_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='watering',
            name='water_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 11, 23, 37, 684895)),
        ),
    ]
