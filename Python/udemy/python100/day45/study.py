# import requests
# from bs4 import BeautifulSoup

# with open('website.html', 'r', encoding='utf-8') as file:
#     html_content = file.read()

# soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.title)

# for tag in soup.find_all(name = "a"):
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find_all(name='h3', class_='heading')
# print(heading)

# soup.find_all

# company_url = soup.select_one(selector="#name")
# print(company_url)

# print(soup.select(selector=".heading"))


import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")

yc = response.text

soup = BeautifulSoup(yc, "html.parser")

articles = soup.find_all(class_="titleline")

article_text = []
article_link = []
article_upvote = []
for article_tag in articles:
    article_text.append(article_tag.getText())
    article_link.append(article_tag.find("a").get("href"))

upvotes = soup.find_all(class_="score")
for votes in upvotes:
    article_upvote.append(int(votes.getText().split(" ")[0]))


# print(article_text)
# print(article_link)
# print(article_upvote)

highest_upvote_index = article_upvote.index(max(article_upvote))

highest_upvote_text = article_text[highest_upvote_index]
highest_upvote_link = article_link[highest_upvote_index]

print(highest_upvote_text)
print(highest_upvote_link)