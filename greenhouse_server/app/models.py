from django.db import models

# from django.utils import timezone


class DHTSensor(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return "t: {} - h: {}".format(self.temperature, self.humidity)


class Watering(models.Model):
    water_request = models.BooleanField(default=False)
    water_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "req: {} - time: {}/{}/{} - at: {}:{}".format(
            self.water_request,
            self.water_time.year,
            self.water_time.month,
            self.water_time.day,
            self.water_time.hour,
            self.water_time.minute,
        )


class Fan(models.Model):
    fan_request = models.BooleanField(default=False)
    fan_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "req: {} - time: {}/{}/{} - at: {}:{}".format(
            self.fan_request,
            self.fan_time.year,
            self.fan_time.month,
            self.fan_time.day,
            self.fan_time.hour,
            self.fan_time.minute,
        )
