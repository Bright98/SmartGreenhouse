# Generated by Django 3.0.7 on 2020-07-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_dhtsensor'),
    ]

    operations = [
        migrations.CreateModel(
            name='DHTSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
            ],
        ),
    ]
