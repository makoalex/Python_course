import requests
from bs4 import BeautifulSoup
import pprint

URL = requests.get("https://www.finn.no/job/fulltime/search.html?location=1.20001.20061&q=Python")
data = BeautifulSoup(URL.text, "html.parser")
contents = data.find_all("article")
# pprint.pprint(contents)
for content in contents:
    job_title = content.find("a").get_text()
    pprint.pprint(job_title)
