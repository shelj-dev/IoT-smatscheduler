from django.urls import path
from . import views 

urlpatterns=[
    # Pico
    path("get-sensor/",views. get_sensor_data,name="get_data"),
    path("send_data/",views.send_sensor_data,name="send_data"),
    # Django
    path("manual/", views.manual_data, name="manual"),
    path("motion_update/",views.motion_update,name="motion_update"),
    path("control/", views.control_page, name="control_page"),        # page
    path("api/control/", views.control_device, name="control_device"), # API
    path("",views.loginForm,name="login"),
    path("sensor_data_api/",views.sensor_data_api,name="sensor_data_api"),
    path("dashboard/",views.dashboard,name="dashboard"),
]