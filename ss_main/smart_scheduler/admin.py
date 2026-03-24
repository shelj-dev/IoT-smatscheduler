from django.contrib import admin
from smart_scheduler.models import ManualSchedule,Motion,SensorData, RelayControls


admin.site.register(ManualSchedule)
admin.site.register(Motion)
admin.site.register(SensorData)
admin.site.register(RelayControls)
