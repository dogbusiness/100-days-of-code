import requests

# Отправляем get запрос на МКС
response = requests.get(url='http://api.open-notify.org/iss-now.json')
# Если сразу напечатать запрос, то получим Response[код ответа]
# print(response)

# У объекта response есть атрибут .status_code - код ответа, собственно
# Конечно, не нужно делать много if elif для обработки исключений - поможет метод
response.raise_for_status()

# Если все хорошо, получаем непосредственно инфу. Мы можем использовать ключ
data = response.json()
longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']
print(data)
print(longitude, latitude)

# Где на карте находится мкс https://www.latlong.net/Show-Latitude-Longitude.html

