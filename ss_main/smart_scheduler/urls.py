from django.urls import path
from . import views 

urlpatterns=[
    path("",views.update,name="update"),
    path("motion_update",views.motion_update,name="motion_update"),
]