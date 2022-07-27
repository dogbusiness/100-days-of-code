import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/news")

web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')

# Single article finding
# article_tag = soup.find(name='a', class_='titlelink') # Или soup.select(selector='.titlelink') НО gettext() не работает
# article_text = article_tag.getText()
# print(article_text)
# article_link = article_tag.get('href')
# print(article_link)
# article_upvote = soup.find(name='span', class_='score').getText()
# print(article_upvote)

# Getting lists of all articles
articles = soup.find_all(name='a', class_='titlelink')

article_texts, article_links = [], []
for article in articles:
    article_text = article.getText()
    article_link = article.get('href')
    article_texts.append(article_text)
    article_links.append(article_link)

# В list comprehension мы используем сплит, берем нулевой индекс (потому что первый будет - 'points'
article_upvotes = [int(score.getText().split(' ')[0]) for score in soup.find_all(name='span', class_='score')]

print(article_texts)
print(article_links)
print(article_upvotes)

# Берем самую популярную
most_popular = f'\n{article_texts[article_upvotes.index(max(article_upvotes))]}' \
               f'\n{article_links[article_upvotes.index(max(article_upvotes))]}'
print(most_popular)