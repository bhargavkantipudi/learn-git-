from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import connection
from .models import displayThermo
from django.shortcuts import render
from json import dumps
from rest_framework import viewsets

# Create your views here.


def indexView(request):
    return render(request,'home.html')

def aboutView(request):
    return render(request,'about.html')

def thermoJoin(request):
    cursor=connection.cursor()
    cursor.execute("select sensor_instances.uid, sensor_instances.sensorid, location_master.locname, location_master.locId from sensor_instances, location_master where sensor_instances.locid=location_master.locid and usensorid='303' ")
    results=cursor.fetchall()
    return render(request,'thermo.html',{'displayThermo':results})

@login_required
def dashboardView(request):
    # details = Devices.objects.all()
    # serializer = DevicesSeriallizer(details,many=true)
    # l = []
    # for x in serializer.data:
    #     temp = dict(x)
    #     l.append(temp)
    # dataJSON = dumps(l)
    return render(request,'dashboard.html')
    #, {"data":details, "dataJson":dataJSON}

@login_required
def deviceView(request):
    return render(request,'icons.html')

@login_required
def ThermoView(request):
    return render(request,'thermo.html')


def registerView(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html',{'form':form})