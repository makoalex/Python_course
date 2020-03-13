import requests
from bs4 import BeautifulSoup
from random import choice
from pprint import pprint


basic_url = "http://quotes.toscrape.com/"
def get_quotes():
    while next_url:
        next_url = "/page/1"
        all_quotes = []
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
def start_game():

    quiz = []
    answer = ' '
    guesses = 4
    quiz.append(choice(all_quotes))
    pprint(quiz)
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
            print("Oops , seems you have ran out of guesses! the name you're looking for is: {}".format(quiz[0]['author']))

    again = ('yes', 'y', 'no', 'n')
    while answer not in again:
        answer = input("Thanks for playing! Would you like to play again y/n?")
    if answer.lower() in ('yes', 'y'):
        return start_game()
    else:
        print('Thanks for playing! Bubye')
