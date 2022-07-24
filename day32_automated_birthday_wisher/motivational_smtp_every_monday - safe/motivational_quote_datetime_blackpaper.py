import smtplib
import datetime as dt
import random as r

#------ Знакомство с datetime ------#
# Устанавливаем день недели с помощью datetime
# Метод now класса datetime позволяет получить текущее время в формате 2022-03-13 16:44:38.250034
# now = dt.datetime.now().weekday()
# Далее мы можем использовать атрибуты например, now.year now.month и метод now.weekday() (конечно можно приписывать)
# Мы можем использовать конкретную дату для if date_of_birth = dt.datetime(year=1999, month=7, day=15, hour=4)
# year, month, day и т.д. это int (SIC!)

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
    # Это пароль, выданный в "Пароли приложений" в аккаунте яндекс. После смены общего пароля, его придется менять!
    yandex_app_password = 'password'
    msg = current_quote
    subject = 'Motivation'
    print(msg)

    connection = smtplib.SMTP('smtp.yandex.ru')
    # TLS - Transport Layer Security (Предшественник SSL и уже устарел)
    connection.starttls()

    # Теперь необходимо войти
    connection.login(user=my_email, password=yandex_app_password)

    # Теперь отправляем имейл. В общем пришел к такой формуле. По-другому яндекс будет считать это спамом и не отправлять
    # Довольно забавно, что погоду делает лишнее \n
    connection.sendmail(from_addr=my_email,
                        to_addrs='email',
                        msg=f'From:{my_email}\nSubject:{subject}\n\n\n{msg}')

    # Закрываем соединение
    connection.close()
