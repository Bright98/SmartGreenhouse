# Generated by Django 3.0.7 on 2020-07-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200722_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fan',
            name='fan_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='watering',
            name='water_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
