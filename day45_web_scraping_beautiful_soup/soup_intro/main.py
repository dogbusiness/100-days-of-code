from bs4 import BeautifulSoup
# Пришлось немного повозиться. Не совсем понятно что надо было устанавливать: bs4 или BeautifulSoup

# import lxml
# Для парсинга lxml необходима другая библиотека. Парсер отсюда работает с некоторыми сайтами. Использовать когда
# Не работает html

with open('website.html') as html:
    contents = html.read()

soup = BeautifulSoup(contents, 'html.parser')

# Мы можем вытягивать определенные html теги с помощью супа.
# Добавляя string мы можем вытянуть то, что в теге. Добавляя name - вытянуть имя тега
# print(soup.title)
# Можно использовать метод prettify чтобы получить красивый размеченный html
# print(soup.prettify())

# Чтобы найти, например, абсолютно все определенные html теги, можно использовать метод find_all. Что
all_anchor_tags = soup.find_all(name='a')

# Чтобы вытянуть только текст в теге, можно использовать цикл с определенным методом getText():
for tag in all_anchor_tags:
    print(tag.getText())