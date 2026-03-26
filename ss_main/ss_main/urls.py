from django.contrib import admin
from django.urls import path,include
from smart_scheduler.views import loginForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('smart_scheduler.urls')),
    path("", loginForm),
]
