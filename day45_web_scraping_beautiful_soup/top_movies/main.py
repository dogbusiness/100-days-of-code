import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
response = response.text

soup = BeautifulSoup(response, 'html.parser')

movies = soup.find_all(name='h3', class_='title')
movies_list = [movie.getText() for movie in movies]
movies_list.reverse()

with open('movies.txt', 'w', encoding='utf-8') as file:
    for movie in movies_list:
        file.write(f'{movie}\n')
