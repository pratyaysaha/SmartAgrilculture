from django.shortcuts import render,HttpResponse
import json
import requests
# Create your views here.

API_KEY="Your API Key"

#Page routes
def home(response):
    return render(response,"index.html")

def irrigation(response):
    return render(response,"irrigation.html")


def cropHealth(response):
    return render(response,"cropHealth.html")

def diseaseDetection(response):
    return render(response,"disease.html")

def weather(response):
    return render(response,"weather.html")

#API for current Weather 
def getWeatherAPI(response):
    if response.method == "POST":
        lat=response.POST['lat']
        lon=response.POST['lon']
        print(lat,lon)
        url = "http://api.openweathermap.org/data/2.5/weather?"
        data = {
            'lat': lat,
            'lon': lon,
            'appid': API_KEY,
            'units': "metric"
        }
        r = requests.get(url=url, params=data)
        context=json.dumps(r.json())
        return HttpResponse(context, content_type="application/json")
        
    return HttpResponse("{'status':'unknown'}", content_type="application/json")

