from django.shortcuts import render
import json
import requests


# Create your views here.
def index(request):
    Weather_data={}


    try:
        if request.method=='POST':
            API_KEY= 'baa3a7a256f02bfe47202ffc079e5245'
            city_name=request.POST['city']

            url='https://api.openweathermap.org/data/2.5/weather'
            parameters={'q':city_name, 'appid':API_KEY, 'units':'metric'}

            response=requests.get(url,parameters)
            response_data= response.json()

            Weather_data={"city" :str(response_data['name']),
                    "country_code": str(response_data['sys']['country']),
                "coordinate": str(response_data['coord']['lon']) + ', '
                + str(response_data['coord']['lat']),
                "temp": str(response_data['main']['temp']) + ' °C',
                "pressure": str(response_data['main']['pressure']),
                "humidity": str(response_data['main']['humidity']),
                'main': str(response_data['weather'][0]['main']),
                'description': str(response_data['weather'][0]['description']),
                'icon': response_data['weather'][0]['icon'],
                'response':True,       
            }
    except:
        Weather_data={"msg": 'Invalid City Name','response':False}
        print("Something went wrong")
   
    return render(request,'WeatherApp/index.html',context=Weather_data)
    