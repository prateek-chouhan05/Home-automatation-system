from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from . import thingspeak
from django.contrib import messages


def home(request):
    if request.method == 'GET':
        if request.GET.get('door'):
            #    print('door')
            thingspeak.updateChannel(1)
        elif request.GET.get('fan'):
            thingspeak.updateChannel(2)
        elif request.GET.get('light1'):
            thingspeak.updateChannel(3)
        elif request.GET.get('light2'):
            thingspeak.updateChannel(4)
    return render(request, "homeautomation/main.html")
