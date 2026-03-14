from django.db import models


class Manual(models.Model):
    onTime=models.TimeField()
    offTime=models.TimeField()
    status = models.BooleanField(default=True)

class Motion(models.Model):
    theshold=models.IntegerField()
    offDelay=models.IntegerField()
    staus=models.BooleanField(default=True)

class sharedData(models.Model):
    light=models.BooleanField(default=True)
    fan=models.BooleanField(default=True)
    # autoMode=models.BooleanField(default=True)

class sensor_data(models.Model):
    sensor_value=models.IntegerField()
    time_stamp=models.DateTimeField( auto_now_add=True)














































