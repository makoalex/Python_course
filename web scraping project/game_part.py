# we are importing the scarping part from csv
from csv import DictReader
from random import choice
from bs4 import BeautifulSoup
import requests

basic_url = "http://quotes.toscrape.com/"


def game(filename):
    with open(filename, 'r') as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            return list(csv_reader)


def start_game(Quotes):
    quiz = []
    answer = ' '
    guesses = 4
    quiz.append(choice(Quotes))
    """we have to create a variable where we can store the get function"""
    question = [el['quote'] for el in quiz][0]
    print([i['author'] for i in quiz][0])
    print(('who said {}  ?'.format(question)))
    while answer.lower().strip() != quiz[0]['author'].lower().strip() and guesses > 0:
        answer = input("Wanna have a go? You have {} remaining guesses`\n".format(guesses))
        if answer.lower() == quiz[0]['author'].lower():
            print("You got it champ!!")
            break
        guesses -= 1
        if guesses == 3:
            result = requests.get("{}{}".format(basic_url, quiz[0]['bio_link']))
            bio = BeautifulSoup(result.text, 'html.parser')
            hint = bio.select(".author-born-date")[0].get_text()
            hint_2 = bio.select(".author-born-location")[0].get_text()
            print("Here is your first hint: The author was born {} on the {}".format(hint_2, hint))
        elif guesses == 2:
            print('Here is another hint: the first letter of his name is {}'.format(quiz[0]['author'][0]))
        elif guesses == 1:
            second_initial = quiz[0]['author'].split()[1][0]
            print('Here is the second letter of his name {}. Good luck!'.format(second_initial))
        else:
            print("Oops , seems you have ran out of guesses! the name you're looking for is: {}".format(
                quiz[0]['author']))

    again = ('yes', 'y', 'no', 'n')
    while answer not in again:
        answer = input("Thanks for playing! Would you like to play again y/n?\n")
    if answer.lower() in ('yes', 'y'):
        return start_game(Quotes)
    else:
        print('Thanks for playing! Bubye')


Quotes = game('Scrape&guess.csv')
start_game(Quotes)
"""there is no more scraping happening anymore, we are using the data saved in the file"""
