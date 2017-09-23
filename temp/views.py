from django.shortcuts import render

import urllib.request
import requests
import json


def get_temp(request):
    return render(request, 'index.html')

def show_temp(request):
    if request.method == "POST":
        zipcode = request.POST['zip']
        r = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',in&appid=aef7dd1902d5faadd042610f94155c59')

        data = json.loads(str(r.read(), 'utf-8'))
        location_name = data['name']
        temp_k = data['main']['temp']
        temp_c = str(int(temp_k) - 273.14)
        return render(request, 'temperature.html', { "zipcode": temp_c, "location": location_name})
