from django.shortcuts import render,HttpResponse
import json
import requests
# Create your views here.

API_KEY="e10945655a16f4e6aceacf3158bd8952"
AGRO_API_KEY="1f8a0e19b649560f257d5009cb66258e"
default_polid="6044e4960573db290cc1c44b"


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

def login(response):
    return render(response,"login.html")

def signup(response):
    return render(response,'signup.html')

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

def getAllWeatherAPI(response):
    if response.method == "POST":
        lat=response.POST['lat']
        lon=response.POST['lon']
        print(lat,lon)
        url = "http://api.openweathermap.org/data/2.5/onecall?"
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

#API for historical NDVI data
def getNDVIAPI(response):
    if response.method=='POST':
        startDate=response.POST['startDate']
        endDate=response.POST['endDate']
        polygonId=response.POST['polid']
        print(startDate,endDate)
        url="http://api.agromonitoring.com/agro/1.0/ndvi/history?"
        data={
            'polyid':default_polid,
            'start':startDate,
            'end':endDate,
            'appid':AGRO_API_KEY
        }
        r=requests.get(url=url,params=data)
        context=json.dumps(r.json())
        return HttpResponse(context,content_type="application/json")
    return HttpResponse("{'status':'unknown'}",content_type='application/json')

def createNewUser(response):
    if response.method=='POST':
        fname=response.POST['fname']
        lname=response.POST['lname']
        username=response.POST['username']
        password=response.POST['password']
        email=response.POST['email']
        print(fname,lname,username,password,email)
        context={'status': 'success'}
        context=json.dumps(context)
        return HttpResponse(context,content_type='application/json')
    return HttpResponse(json.dumps("{'status': 'forbidden'}"),content_type='application/json')
    


