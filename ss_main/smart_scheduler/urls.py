from django.urls import path
from . import views 

urlpatterns=[
    path("",views.update,name="update"),
    path("motion_update/",views.motion_update,name="motion_update"),
    path("get-sensor/",views. get_sensor_data,name="get_data"),
    path("send_data/",views.send_sensor_data,name="send_data"),
]