# Generated by Django 3.0.7 on 2020-07-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20200722_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='fan',
            name='fan_request',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fan',
            name='fan_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='watering',
            name='water_request',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='watering',
            name='water_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]