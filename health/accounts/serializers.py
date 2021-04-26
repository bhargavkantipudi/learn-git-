from rest_framework import serializers
from .models import Devices

class DevicesSeriallizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Devices
        fields = ('Gate_No', 'Thermometer_Id','Thermometer_Status','Thermometer_Last_Active','Oximeter_Id', 'Oximeter_Status', 'Oximeter_Last_Active')



        