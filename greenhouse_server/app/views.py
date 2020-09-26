from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
import datetime
from .models import DHTSensor, Watering, Fan


def all_dhtSensor(request, dht_id):
    data = DHTSensor.objects.get(id=dht_id)
    contex = {
        "temperature": str(data.temperature),
        "humidity": str(data.humidity),
    }
    return JsonResponse(contex, safe=False)


def all_watering(request, water_id):
    data = Watering.objects.get(id=water_id)
    contex = {
        "status": str(data.water_request),
        "watering_month": str(data.water_time.month),
        "watering_day": str(data.water_time.day),
        "watering_hour": str(data.water_time.hour),
        "watering_minute": str(data.water_time.minute),
    }
    return JsonResponse(contex, safe=False)


def all_fan(request, fan_id):
    data = Fan.objects.get(id=fan_id)
    contex = {
        "status": str(data.fan_request),
        "fan_month": str(data.fan_time.month),
        "fan_day": str(data.fan_time.day),
        "fan_hour": str(data.fan_time.hour),
        "fan_minute": str(data.fan_time.minute),
    }
    return JsonResponse(contex, safe=False)


@csrf_exempt
def last_dhtSensor(request):
    if request.method == "POST":

        new_dht = json.loads(request.body.decode("utf-8"))
        self_temperature = new_dht["temperature"]
        self_humidity = new_dht["humidity"]

        data = DHTSensor(temperature=self_temperature, humidity=self_humidity)
        data.save()

    elif request.method == "GET":
        data = DHTSensor.objects.latest("id")

    contex = {
        "temperature": str(data.temperature),
        "humidity": str(data.humidity),
    }
    return JsonResponse(contex, safe=False)


@csrf_exempt
def last_watering(request):
    if request.method == "POST":

        if request.POST:
            new_watering = request.POST
            water_req = new_watering["water_request"]
        else:
            new_watering = json.loads(request.body.decode("utf-8"))
            water_req = new_watering["status"]

        water_self_time = datetime.datetime.now()

        w = Watering(water_request=water_req, water_time=water_self_time)
        w.save()

    elif request.method == "GET":
        w = Watering.objects.latest("id")

    contex = {
        "status": str(w.water_request),
        "watering_month": str(w.water_time.month),
        "watering_day": str(w.water_time.day),
        "watering_hour": str(w.water_time.hour),
        "watering_minute": str(w.water_time.minute),
    }
    return JsonResponse(contex, safe=False)


@csrf_exempt
def last_fan(request):
    if request.method == "POST":

        if request.POST:
            new_fan = request.POST
            fan_req = new_fan["fan_request"]
        else:
            new_fan = json.loads(request.body.decode("utf-8"))
            fan_req = new_fan["status"]

        fan_self_time = datetime.datetime.now()

        f = Fan(fan_request=fan_req, fan_time=fan_self_time)
        f.save()

    elif request.method == "GET":
        f = Fan.objects.latest("id")

    contex = {
        "status": str(f.fan_request),
        "fan_month": str(f.fan_time.month),
        "fan_day": str(f.fan_time.day),
        "fan_hour": str(f.fan_time.hour),
        "fan_minute": str(f.fan_time.minute),
    }
    return JsonResponse(contex, safe=False)
