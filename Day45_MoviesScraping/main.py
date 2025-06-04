from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, 'html.parser')

post_title = soup.find_all(class_="titleline")

for i in post_title:
    print(i.text)
    print(i.a['href'])

upvote_number = soup.find_all(class_="score")

for i in upvote_number:
    print(i.text)