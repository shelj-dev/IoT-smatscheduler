from django.contrib import admin
from smart_scheduler.models import Manual,Motion,sharedData,sensor_data


admin.site.register(Manual)
admin.site.register(Motion)
admin.site.register(sharedData)
admin.site.register(sensor_data)
