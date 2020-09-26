from django.urls import path
from . import views


urlpatterns = [
    # path("", views.homePage),
    path("dht_sensor/<int:dht_id>", views.all_dhtSensor),
    path("watering/<int:water_id>", views.all_watering),
    path("fan/<int:fan_id>", views.all_fan),
    path("dht_sensor/", views.last_dhtSensor),
    path("watering/", views.last_watering),
    path("fan/", views.last_fan),
]
