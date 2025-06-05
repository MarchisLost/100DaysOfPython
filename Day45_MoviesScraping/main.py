from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, 'html.parser')

post_title = soup.find_all(class_="titleline")

articles_texts = []
articles_links = []
for i in post_title:
    articles_texts.append(i.text)
    articles_links.append(i.a['href'])

upvote_number = [int(i.text.split()[0]) for i in soup.find_all(class_="score")]

max_upvote = max(upvote_number)
max_upvote_index = upvote_number.index(max_upvote)
print(articles_texts[max_upvote_index])
print(articles_links[max_upvote_index])
print(upvote_number[max_upvote_index])
