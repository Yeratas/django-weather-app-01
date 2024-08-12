from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm
import requests as req

def home(request):
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CityForm()
    
    cities_list = City.objects.all()
    
    api_key = 'XXXXXXXXXXXXXXXXXXXXXXXX'
    # can get your own api at https://openweathermap.org/api
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key

    weather_list = []
    
    for city in cities_list:
        resp = req.get(url.format(city)).json()
        weather_info = {
            'city': city,
            'country': str(resp['sys']['country']),
            'temp': str(resp['main']['temp']),
            # 'temp_min': str(resp['main']['temp_min']),
            # 'temp_max': str(resp['main']['temp_max']),
            'wind_speed': resp['wind']['speed'],
            'description': str(resp['weather'][0]['description']),
            'icon': resp['weather'][0]['icon']
        }
        weather_list.append(weather_info)
        print(cities_list)
    context = {
        'form':form,
        'weather_list':weather_list,
        'cities_list':cities_list
        }
    return render(request,'home.html',context)

def delete_record(request,city):
    city = City.objects.get(name=city)
    city.delete()
    return redirect('home')