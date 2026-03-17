from django.shortcuts import render,redirect,get_object_or_404
from smart_scheduler.forms import ManualForm,MotionForm
from smart_scheduler.models import Manual,Motion,sharedData, sensor_data
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.utils import timezone
from datetime import datetime



def update(request):
    data=get_object_or_404(Manual,1)
    if request.method=="POST":
        time=ManualForm(request.POST,instance=data)
        if time.is_Vaild():
            time.save
            return redirect("update")
    else:
        time=ManualForm()
    return render(request,"update.html",{'time':time})


def motion_update(request):
    data=get_object_or_404(Motion,1)
    if request.method=="POST":
        time=MotionForm(request.POST,instance=data)
        if time.is_Vaild():
            time.save
            return redirect("update")
    else:
        time=MotionForm()
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
    sensor = Motion.objects.first()
    control = sharedData.objects.first()

    now = timezone.localtime()

    on_time = timezone.make_aware(
        datetime.combine(now.date(), schedule.onTime)
    )

    off_time = timezone.make_aware(
        datetime.combine(now.date(), schedule.offTime)
    )
    schedule_on_light = False
    schedule_off_light = False

    if on_time <= off_time:
        if on_time <= now <= off_time:
            schedule_on_light = True
        else:
            schedule_off_light = True
    else:
        if now >= on_time or now <= off_time:
            schedule_on_light = True
        else:
            schedule_off_light = True

    data = {
        "schedule_automode": schedule.status,
        "schedule_on_time": schedule_on_light,
        "schedule_off_time": schedule_off_light,
        "sensor_automode": sensor.status,
        "sensor_threshold": sensor.threshold,
        "sensor_off_delay": sensor.offDelay,
        "light": control.light,
        "fan": control.fan
    }

    print(data)
    return JsonResponse(data)

