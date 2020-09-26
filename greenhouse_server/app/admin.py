from django.contrib import admin
from .models import DHTSensor, Watering, Fan


admin.site.register(DHTSensor)
admin.site.register(Watering)
admin.site.register(Fan)
