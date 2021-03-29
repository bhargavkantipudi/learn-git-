from django.db import models
from django.utils import timezone


class Devices(models.Model):
	Gate_No = models.IntegerField()
	Thermometer_Id = models.IntegerField()
	Thermometer_Status = models.BooleanField()
	Thermometer_Last_Active = models.DateTimeField(default=timezone.now)
	Oximeter_Id = models.IntegerField()
	Oximeter_Status = models.BooleanField()
	Oximeter_Last_Active = models.DateTimeField(default=timezone.now)

