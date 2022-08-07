import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ПЕРЕНЕСТИ ПОТОМ В ENV
client_id = '...'
client_secret = '...'
scope = 'user-read-recently-played'

year = 2001 #input()

response = requests.get(f'https://playback.fm/charts/top-100-songs/{year}')

if response.status_code != 200:
    print(response.status_code)
else:
    print('Все ок')

soup = BeautifulSoup(response.text, 'html.parser')


tracks = soup.find_all(name='a', itemprop='name')
track_list = [track.getText().replace('\n', '') for track in tracks]
print(track_list)

artists = soup.find_all(name='a', class_='artist')
artist_list = [artist.getText().replace('\n', '') for artist in artists]
print(artist_list)

token1 = spotipy.oauth2.SpotifyOAuth(client_id='7f9e0c11e5cc4f98b7b43efe8957c027',
                                    client_secret='331b3219e0df4c249d39b3edccbd6e2c',
                                    scope='playlist-modify-private', redirect_uri='https://example.com/')

user_id = spotipy.Spotify(auth_manager=token1).current_user()['id']
print(user_id)

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='7f9e0c11e5cc4f98b7b43efe8957c027', client_secret='331b3219e0df4c249d39b3edccbd6e2c',
#                                                scope='playlist-modify-private', redirect_uri='https://example.com/'))


