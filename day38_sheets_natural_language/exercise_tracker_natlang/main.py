import requests, datetime

# CONSTANTS
APP_ID = '8cca18aa'
API_KEY = 'a4d874a6107c1d426d21f75a7c3abab5'

# Exercise description with natural language
exer_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
# Непосредственно распознание натурального языка здесь в параметре query
user_input = input('Что сделал?: ')
params = {
    'query': user_input,
    'gender': 'male',
    'weight_kg': 63.0,
    'height_cm': 170.0,
    'age': 22
}
response = requests.post(url=exer_endpoint, headers=headers, json=params)
response_json = response.json()
print(response_json)
date_now = datetime.datetime.now().strftime('%d/%m/%Y')
time_now = datetime.datetime.now().strftime('%H:%M')
try:
    duration = response_json['exercises'][0]['duration_min']
    exercise = response_json['exercises'][0]['user_input']
    calories = response_json['exercises'][0]['nf_calories']
except KeyError:
    print('Oops. Something went wrong')
else:
    # Работаем с Sheety API
    sheety_token = 'asgbj23g5hkasjd1jh2lkjhasd'
    sheety_endpoint = 'https://api.sheety.co/6152012fa02524ae289efe2cbb0d2588/myWorkouts/workouts'
    header = {'Authorization': 'Bearer asgbj23g5hkasjd1jh2lkjhasd'}
    payload = {
        'workout': {
            'date': date_now,
            'time': time_now,
            'duration': duration,
            'exercise': exercise.title(),
            'calories': calories
        }
    }
    response = requests.post(url=sheety_endpoint, headers=header, json=payload)
    print(response.json())



