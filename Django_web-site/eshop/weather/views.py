from django.shortcuts import render
from pyowm import OWM
import requests


# Create your views here.

def weather(request):
    return render(request, 'weather/weather.html', {
        'page': 'weather'
    })

def weather_result(request):
    try:
        city = request.GET.get('city')
        owm = OWM('1f0edccac75d4e289b22f081fdbef188')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(str(city))
        w = observation.weather
        return render(request, 'weather/weather.html', {
            'page': 'weather',
            'city': city,
            'status': w.detailed_status,
            'wind': w.wind,
            'temp': w.temperature('celsius'),
            'clouds': w.clouds
        })
    except Exception:
        return render(request, 'weather/weather.html', {
            'page': 'weather',
            'error': True
        })