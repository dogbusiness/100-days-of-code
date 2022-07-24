import smtplib
import datetime as dt
import random as r

#------ Мотивашка ------#
# Получаем список мотивашек с помощью readlines
# В формате ['"Цитата"  - Marcus Aurelius\n', следующая цитата
with open('quotes.txt') as quotes:
    quotes_list = [quote for quote in quotes.readlines()]

#------ SMTP and DateTime ------#
now_weekday = dt.datetime.now().weekday()
if now_weekday == 6:
    # Засунем текущую цитату сюда, чтобы лишний раз не занимать память (если день не текущий)
    current_quote = r.choice(quotes_list)

    my_email = 'email'
    yandex_app_password = 'xbcanufiuyquoako'

    msg = current_quote
    subject = 'Motivation'

    # Порт указывается сразу после smtp address 'smtp.yandex.ru: 487'
    # Не указываю его, потому что иначе яндекс посчитает сообщение спамом ¯\_(ツ)_/¯
    connection = smtplib.SMTP('smtp.yandex.ru')
    connection.starttls()
    connection.login(user=my_email, password=yandex_app_password)

    # Непонятен алгоритм признания сообщения спамом (Яндекс). Погоду делают три новых строки ¯\_(ツ)_/¯
    connection.sendmail(from_addr=my_email,
                        to_addrs='email',
                        msg=f'From:{my_email}\nSubject:{subject}\n\n\n{msg}')

    # Закрываем соединение
    connection.close()
