import requests
import os
# one_call_api_request = 'https://api.openweathermap.org/data/2.5/onecall'
# prepod_api_key = '69f04e4613056b159c2761a9d9e664d2'
parameters = {
    'appid': 'something',
    'lon': 39.17,
    'lat': 51.6664,
    'exclude': 'current,minutely',
    'units': 'metric'
}

# Sending request
response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

# Forming twelve hours forecast
twelve_hours = [weather_data['hourly'][i]['weather'][0]['id'] for i in range(0, 11)]
print(twelve_hours)
# for item in twelve_hours:
#     if item < 803:
#         print('Clear Sky')

