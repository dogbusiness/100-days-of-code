import requests
import datetime
import smtplib

vrn_lat = 51.677073
vrn_lng = 39.176903
current_hour = datetime.datetime.now().hour

my_email = 'email'
yandex_app_password = 'password'
smtp_server = 'smtp.yandex.ru'
subject = 'MKS nad tvoey golovoi'

parameters_sun = {
    'lat': vrn_lat,
    "lng": vrn_lng,
    'formatted': 0
}

# Sunrise Sunset API
response_sun = requests.get('https://api.sunrise-sunset.org/json', params=parameters_sun)
response_sun.raise_for_status()
data_sun = response_sun.json()

sunrise = int(data_sun['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data_sun['results']['sunset'].split('T')[1].split(':')[0])

# ISS API
response_iss = requests.get(url='http://api.open-notify.org/iss-now.json')
response_iss.raise_for_status()
data_iss = response_iss.json()

iss_lat = float(response_iss.json()['iss_position']['longitude'])
iss_lng = float(response_iss.json()['iss_position']['latitude'])


# DEBUG #
# iss_lat = 47.677073
# iss_lng = 43.176903
# sunset, current_hour, sunrise = 15, 23, 3
# Положение МКС
if vrn_lat - 5 <= iss_lat <= vrn_lat + 5 and vrn_lng - 5 <= iss_lng <= vrn_lng + 5:
    print('True')
    # Темное время суток
    if current_hour >= sunset or current_hour <= sunrise:
        # Отправляем сообщение
        print('Отправляю')
        connection = smtplib.SMTP(smtp_server)
        connection.starttls()
        connection.login(user=my_email, password=yandex_app_password)

        message = f'From:{my_email}\nSubject:{subject}\n\nLook up!'

        connection.sendmail(
            from_addr=my_email,
            to_addrs='sergeusprecious@gmail.com',
            msg=message
        )

        connection.close()






