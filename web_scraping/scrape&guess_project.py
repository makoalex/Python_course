import requests
from bs4 import BeautifulSoup
from random import choice
from pprint import pprint

all_quotes = []
quiz = []
answer = []
guesses = 4
basic_url = "http://quotes.toscrape.com/"
next_url = "/page/1"
while next_url:
    url = requests.get("{}{}".format(basic_url, next_url))
    # print("now scrapping {}{}".format(basic_url, next_url))
    data = BeautifulSoup(url.text, "html.parser")
    quotes = data.select(".quote")

    for q in quotes:
        all_quotes.append({"quote": q.find('span').get_text(),
                           "author": q.select(".author")[0].get_text(),
                           "bio_link": q.find('a')['href']

                           })

    next_button = data.find(class_="next")
    next_url = next_button.find_next("a")["href"] if next_button else None

    quiz.append(choice(all_quotes))
    pprint(quiz)
    question = [el['quote'] for el in quiz][0]
    print(input('who said {} ?'.format(question)))
    if answer == [a['author'] for a in quiz][0]:
        print('Congratulations ! Your answer is correct')
    elif not answer:
        guesses -= 1
        if guesses == 3:
            print('YOU HAVE 3 GUESSES LEFT !')
            hint = data.find_all(class_='text')[0].find_next_sibling()
            print(hint)
            print(len(hint))
