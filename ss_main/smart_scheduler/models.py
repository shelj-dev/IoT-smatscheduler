from django.db import models


class ManualSchedule(models.Model):
    """Turn on or off on the scheduled time"""
    onTime=models.TimeField()
    offTime=models.TimeField()
    status = models.BooleanField(default=True)

    # class Meta:
    #     verbose_name = "Manual Schedule"
    #     verbose_name_plural = "Manual Schedules"


class Motion(models.Model):
    """This controls motion control mode"""
    threshold=models.IntegerField()
    offDelay=models.IntegerField()
    status=models.BooleanField(default=True)

    # class Meta:
    #     verbose_name = "Motion Schedule"
    #     verbose_name_plural = "Motion Schedules"


class RelayControls(models.Model):
    """This controls  the device light or fan"""
    light=models.BooleanField(default=True)
    fan=models.BooleanField(default=True)

    # class Meta:
    #     verbose_name = "Lights ON OFF control"
    #     verbose_name_plural = "Lights ON OFF controls"


class SensorData(models.Model):
    """Stores data from the pico"""
    sensor_value=models.IntegerField()
    time_stamp=models.DateTimeField( auto_now_add=True)

    # class Meta:
    #     verbose_name = "Motion mode control"
    #     verbose_name_plural = "Motion mode controls"













































