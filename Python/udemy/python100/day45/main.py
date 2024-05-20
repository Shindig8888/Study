import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movie = response.text

soup = BeautifulSoup(movie, "html.parser", from_encoding='utf-8')

movies = soup.find_all(class_="article-title-description__text")

print(movies)

movie_list = []
for movie in movies:
    movie_list.append(movie.find(class_="title").string.encode('utf-8'))

movie_list = movie_list[::-1]

print(movie_list)

with open("movie.txt", 'w') as file:
    for movie in movie_list:
        file.write(f"{movie}\n")