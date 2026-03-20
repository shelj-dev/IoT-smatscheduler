from django.urls import path
from . import views 

urlpatterns=[
    # path("",views.update,name="update"),
    path("motion_update/",views.motion_update,name="motion_update"),
    path("get-sensor/",views. get_sensor_data,name="get_data"),
    path("send_data/",views.send_sensor_data,name="send_data"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("sensor_data_api/",views.sensor_data_api,name="sensor_data_api"),
    path("manual/", views.manual_Data, name="manual"),
    path("control/", views.control_page, name="control_page"),        # page
    path("api/control/", views.control_device, name="control_device"), # API
    path("",views.loginForm,name="login")
]