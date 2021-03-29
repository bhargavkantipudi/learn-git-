from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Devices
from django.shortcuts import render
from json import dumps

# Create your views here.


def indexView(request):
    return render(request,'index.html')

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

def registerView(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html',{'form':form})