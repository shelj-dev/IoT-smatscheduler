from django.shortcuts import render,redirect,get_object_or_404,redirect
from smart_scheduler.forms import ManualScheduleForm,MotionForm,LoginForm
from smart_scheduler.models import ManualSchedule,Motion,RelayControls, SensorData
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from datetime import timedelta



def manual_data(request):
    """
    to update the sensor data
    """
    data=ManualSchedule.objects.first()
    if request.method=="POST":
        time=ManualScheduleForm(request.POST,instance=data)
        if time.is_valid():
            time.save()
            print("Success")
            return redirect("manual")
    else:
        time=ManualScheduleForm(instance=data)
    return render(request,"manual.html",{'time':time})


def motion_update(request):
    """data to update to motion"""
    data=get_object_or_404(Motion,1)
    if request.method=="POST":
        time=MotionForm(request.POST,instance=data)
        if time.is_valid():
            time.save()
            return redirect("update")
    else:
        time=MotionForm()
    return render(request,"update.html",{'time':time})

def control_page(request):
    return render(request, "control_device.html") 

def control_device(request):
    data = RelayControls.objects.first()

    if not data:
        data = RelayControls.objects.create()

    device = request.GET.get("device")
    action = request.GET.get("action")

    if device == "light":
        data.light = (action == "on")
    elif device == "fan":
        data.fan = (action == "on")

    data.save()

    return JsonResponse({
        "status": "success",
        "device": device,
        "action": action
    })

@csrf_exempt
def get_sensor_data(request):
    """sensor data  to jason formate"""

    if request.method == "POST":
        data = json.loads(request.body)

        value = data.get("sensor")
        SensorData.objects.create(sensor_value=value)

        return JsonResponse({
            "status": "received",
            "sensor": value
        })

    return JsonResponse({"error": "POST required"})


@require_GET
def send_sensor_data(request):
    schedule = ManualSchedule.objects.first()
    sensor = Motion.objects.first()
    control = RelayControls.objects.first()

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

def loginForm(request):
    if request.method== "POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("dashboard")
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{"form":form})


def sensor_data_api(request):
    
    data = SensorData.objects.order_by('-time_stamp')[:1]  

    is_connected = False
    response_data = []

    if data:
        last_record = data[0]
        now = timezone.now()

        # ✅ FIXED field name
        is_connected = last_record.time_stamp >= now - timedelta(seconds=7)

        # ✅ Convert queryset to JSON serializable list
        for d in data:
            response_data.append({
                "value": d.sensor_value,
                "time": d.time_stamp.strftime("%H:%M:%S")
            })

    return JsonResponse({
        "data": response_data,
        "is_connected": is_connected
    })


def dashboard(request):
    data = SensorData.objects.order_by('-time_stamp')[:10]
    motion = Motion.objects.first()
    print(data)
    if request.method == "POST":
        form=MotionForm(request.POST, instance=motion)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form=MotionForm(instance=motion)   
    return render(request,"dashboard.html", {"data": data, "form":form})