from django.db import models


class ManualSchedule(models.Model):
    """Turn on or off on the scheduled time"""
    onTime=models.TimeField()
    offTime=models.TimeField()
    status = models.BooleanField(default=True)

    

class Motion(models.Model):
    """This controls motion control mode"""
    threshold=models.IntegerField()
    offDelay=models.IntegerField()
    status=models.BooleanField(default=True)

    


class RelayControls(models.Model):
    """This controls  the device light or fan"""
    light=models.BooleanField(default=True)
    fan=models.BooleanField(default=True)

    

class SensorData(models.Model):
    """Stores data from the pico"""
    sensor_value=models.IntegerField()
    time_stamp=models.DateTimeField( auto_now_add=True)













































