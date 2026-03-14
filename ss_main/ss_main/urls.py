from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('smart_scheduler/',include('smart_scheduler.urls')),
]
