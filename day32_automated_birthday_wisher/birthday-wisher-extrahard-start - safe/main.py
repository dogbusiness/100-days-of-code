##################### Extra Hard Starting Project ######################
import pandas
import time
import datetime as dt
import smtplib
import random

#------ CONSTANTS ------#
now_month = dt.datetime.now().month
now_day = dt.datetime.now().day
my_email = 'email'
yandex_app_password = 'password'
smtp_server = 'smtp.yandex.ru'
subject = 'Happy Birthday!'

#------ Reading CSV ------#
birth_csv = pandas.read_csv('birthdays.csv')
bdays_list = birth_csv.to_dict(orient='records')
# Формат [{'name': 'Test', 'email': 'sergeusprecious@gmail.com', 'year': 1999, 'month': 3, 'day': 13}, ...

for item in bdays_list:
    try:
        if item['month'] == now_month and item['day'] == now_day:
            # Читаем рандомный темплейт письма
            print(item['day'])
            print(item['month'])
            print(now_day)
            print(now_month)
            temp_num = random.randint(1, 3)
            with open(f'letter_templates/letter_{temp_num}.txt') as template:
                letter = template.read()
                # Вставляем имя именинника в текст письма вместо [NAME]
                letter = letter.replace('[NAME]', item['name'])
            # Наконец, используем SMTP, на всякий случай используя sleep
            connection = smtplib.SMTP(smtp_server)
            connection.starttls()
            connection.login(user=my_email, password=yandex_app_password)

            message = f'From:{my_email}\nSubject:{subject}\n\n{letter}'

            connection.sendmail(
                from_addr=my_email,
                to_addrs=item['email'],
                msg=message
            )

            connection.close()
            time.sleep(60.0)
    except KeyError:
        print(KeyError)

