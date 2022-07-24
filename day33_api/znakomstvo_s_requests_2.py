import requests
import datetime
# Учимся пользоваться параметрами на примере Sunset and sunrise times API
vrn_lat = 51.677073
vrn_lng = 39.176903

parameters = {
    'lat': vrn_lat,
    "lng": vrn_lng,
    'formatted': 0
}

# Мы можем указать необходимые параметры запроса таким образом. Возможно используя амперсан и вопрос знак
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
# Получаем час через сплит
print(sunrise.split('T')[1].split(':')[0], sunset.split('T')[1].split(':')[0], sep='\n')
print(datetime.datetime.now().hour)