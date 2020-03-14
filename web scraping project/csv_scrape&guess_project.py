# copying the scraped data to a CSV file so we can recall it whenever we want
# we will move functionality to another file because we dint want to be saving to the csv file everytime
import requests
from bs4 import BeautifulSoup
from random import choice
from pprint import pprint
from csv import DictWriter
import io

basic_url = "http://quotes.toscrape.com/"


def get_quotes():
    next_url = "/page/1"
    all_quotes = []
    while next_url:
        url = requests.get("{}{}".format(basic_url, next_url))
        data = BeautifulSoup(url.text, "html.parser")
        quotes = data.select(".quote")
        for q in quotes:
            all_quotes.append({"quote": q.find('span').get_text(),
                               "author": q.select(".author")[0].get_text(),
                               "bio_link": q.find('a')['href']
                               })
        next_button = data.find(class_="next")
        next_url = next_button.find_next("a")["href"] if next_button else None
    return all_quotes
Quotes = get_quotes()
"""write the quotes to a csv file now using Dictwriter"""
with io.open('Scrape&guess_Project.csv','w',encoding='utf-8', newline='')as file:
    headers = ['quote', 'author', 'bio_link']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for q in Quotes:
        csv_writer.writerow(q)