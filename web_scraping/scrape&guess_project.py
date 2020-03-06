import requests
from bs4 import BeautifulSoup

import pprint

all_quotes = []
link = []
writers = []
basic_url= "http://quotes.toscrape.com/"
next_url = "/page/1"


url = requests.get("{}{}".format(basic_url, next_url))
data = BeautifulSoup(url.text, "html.parser")
quotes = data.select(".quote")

for q in quotes:
    Quote = q.find('span').get_text()
    all_quotes.insert(0, Quote)
    print((all_quotes))
    author = q.select(".author")[0].get_text()
    writers.insert(0, author)
    # print(writers)
    bio_link = q.find('a')['href']
    # print(bio_link)
    link.append(bio_link)
    # print(link)
    next_button = data.find_all(class_="next")
    next_url = next_button.find("a")["href"]

