# Generated by Django 3.0.7 on 2020-07-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200721_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fan',
            name='fan_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
