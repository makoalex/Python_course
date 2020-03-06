
import requests
import pprint
from bs4 import BeautifulSoup
from csv import writer

Url = requests.get("https://www.rithmschool.com/blog")
data = BeautifulSoup(Url.text, "html.parser")
articles = data.find_all("article")

with open("blog_data.csv", 'w', newline="")as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["TITLE", " LINK", "DATE"])
    for article in articles:
        title = article.find("a").get_text()  # getting the title of the anchor tag
        href = article.select("[href]")[1].attrs["href"]
        time = article.select("[datetime]")[0].attrs["datetime"]
        time1 = article.find("time")["datetime"]
        csv_writer.writerow([title, href, time1])
