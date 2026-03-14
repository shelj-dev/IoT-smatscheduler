from django.shortcuts import render,redirect,get_object_or_404
from smart_scheduler.forms import ManualForm
from smart_scheduler.models import Manual,Motion,sharedData, sensor_data
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET


def update(request):
    data=get_object_or_404(Manual,1)
    if request.method=="POSt":
        time=ManualForm(request.POST,instence=data)
        if time.is_vaild():
            time.save
            return redirect("update")
    else:
        time=ManualForm()
    return render(request,"update.html",{'time':time})


def motion_update(request):
    data=get_object_or_404(Manual,1)
    if request.method=="POSt":
        time=ManualForm(request.POST,instence=data)
        if time.is_vaild():
            time.save
            return redirect("update")
    else:
        time=ManualForm()
    return render(request,"update.html",{'time':time})


@csrf_exempt
def get_sensor_data(request):

    if request.method == "POST":
        data = json.loads(request.body)

        value = data.get("sensor")
        sensor_data.objects.create(sensor_value=value)

        return JsonResponse({
            "status": "received",
            "sensor": value
        })

    return JsonResponse({"error": "POST required"})


@require_GET
def send_sensor_data(request):
    schedule = Manual.objects.first()
    sensor=Motion.objects.first()
    control=sharedData.objects.first()
    data = {
        "schedule_automode": schedule.status,
        "schedule_on_time": schedule.onTime,
        "schedule_off_time": schedule.offTime,
        "sensor_automode": sensor.staus,
        "sensor_threshold": sensor.theshold,
        "sensor_off_delay": sensor.offDelay,
        "light":control.light ,
        "fan": control.fan
    }
    return JsonResponse(data)