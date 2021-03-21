from django.shortcuts import render,HttpResponse
import json
import requests
# Create your views here.

API_KEY="e10945655a16f4e6aceacf3158bd8952"

#Page routes
def home(response):
    return render(response,"index.html")

def irrigation(response):
    return HttpResponse("This is irrigation")


def cropHealth(response):
    return HttpResponse("This is crop health")

def diseaseDetection(response):
    return HttpResponse("This is disease detection")

def weather(response):
    return HttpResponse("This is weather")

#API for current Weather 
def getWeatherAPI(response):
    if response.method == "POST":
        city=response.POST['city']
        print(city)
        url = "http://api.openweathermap.org/data/2.5/weather?"
        data = {
            'q': city,
            'appid': API_KEY,
            'units': "metric"
        }
        r = requests.get(url=url, params=data)
        context=json.dumps(r.json())
        return HttpResponse(context, content_type="application/json")
        
    return HttpResponse("{'status':'unknown'}", content_type="application/json")

