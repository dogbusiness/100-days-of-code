import smtplib

my_email = 'email'
# Это пароль, выданный в "Пароли приложений" в аккаунте яндекс. После смены общего пароля, его придется менять!
yandex_app_password = 'password'
msg = 'Hi! I am testing SMTP'
subject = 'Test'

connection = smtplib.SMTP('smtp.yandex.ru')
# TLS - Transport Layer Security (Предшественник SSL и уже устарел)
connection.starttls()

# Теперь необходимо войти
connection.login(user=my_email, password=yandex_app_password)

# Теперь отправляем имейл. В общем пришел к такой формуле. По-другому яндекс будет считать это спамом и не отправлять
# Довольно забавно, что погоду делает лишнее \n
connection.sendmail(from_addr=my_email,
                    to_addrs='email',
                    msg=f'From:{my_email}\nSubject:{subject}\n\nI am tired of testing')

# Закрываем соединение
connection.close()
