import requests, datetime

USERNAME = 'USERNAME'
TOKEN = 'TOKEN'

pixela_endpoint = 'https://pixe.la/v1/users'
user_page = 'https://pixe.la/@username'

user_params = {
    'token': 'token',
    'username': 'username',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# Уже создал нового пользователя, так что комменчу
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Создаем новый граф
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': 'graph1',
    'name': 'cigarettes',
    'unit': 'Cigs',
    'type': 'int',
    'color': 'ajisai'
}
headers = {
    'X-USER-TOKEN': TOKEN
}
# Наконец-то вкладываем значения в header и создаем граф
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# Граф - https://pixe.la/v1/users/dog0business/graphs/graph1.html

# Вставляем пиксель в граф используя datetime
now = datetime.datetime.now()
add_pixel_endpoint = 'https://pixe.la/v1/users/dog0business/graphs/graph1'
pixel_params = {
    'date': now.strftime('%Y%m%d'),
    'quantity': '5'
}
response = requests.post(url=add_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
