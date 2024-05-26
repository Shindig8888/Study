import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

CLIENTID = os.getenv("CLIENTID")

CLIENTSECRETE = os.getenv("CLIENTSECRETE")

year = input("Which year do you want to travel? YYYY-MM-DD: ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{year}")
billboard = response.text

soup = BeautifulSoup(billboard, "html.parser")

targets = soup.find_all(class_="o-chart-results-list__item")

song_list = []
artist_list = []

for item in targets:
    if item. find(class_="c-title", id="title-of-a-story") != None:
        song_list.append(item. find(class_="c-title", id="title-of-a-story").string.strip())
        artist_list.append(item.find(class_="c-label").string.strip())
print(song_list)
print(artist_list)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENTID,
                                               client_secret=CLIENTSECRETE,
                                               scope="playlist-modify-public user-library-modify",
                                               redirect_uri="https://example.com"
                                               ))

song_url_list = []
for n in range(0, len(song_list)):
    result = sp.search(q=f"track: {artist_list[n]} {song_list[n]} year: {year[:4]}", limit=20)
    song_url_list.append(result['tracks']['items'][0]['external_urls']['spotify'])

pprint(song_url_list)

print(sp.current_user())

playlist_name = f"{year} Billboard 100"
user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(user=user_id, name=playlist_name)

print("Playlist created successfully!")
print("Playlist ID:", playlist["id"])

sp.user_playlist_add_tracks(user="user_id", playlist_id=playlist["id"], tracks=song_url_list)

playlist = sp.user_playlist(user="user_id", playlist_id=playlist["id"])
pprint(playlist)

