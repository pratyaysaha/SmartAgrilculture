from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('irrigation', views.irrigation,name='irrigation'),
    path('cropHealth', views.cropHealth,name='cropHealth'),
    path('dieaseDetection', views.diseaseDetection,name='disease'),
    path('weather', views.irrigation,name='weather'),
    path('api/getCurWeather',views.getWeatherAPI,name="CurWeatherAPI")
]
