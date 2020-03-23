from csv import DictWriter
from random import choice


class Question:
    def __init__(self, question):
        self.question = question

    def __repr__(self):
        return "Green is a versatile word: it can be a noun, adjective, or verb;\n" \
               " we earn greenbacks to buy greens in the market \n" \
               "(locally sourced and organic, of course, to be as green as we can be)\nOh yeah, and it's a color too."

    def ask_question(self):


with open('quiz.csv', 'a', newline="") as file:
    headers = [' QUESTION ', ' OPTION I ', ' OPTION II ', ' OPTION III ', ' OPTION IV ']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writerow({
        ' QUESTION ': 'Where is a GREEN MOUNTAIN BOY from?',
        ' OPTION I ': 'VERMONT',
        ' OPTION II ': 'BRITISH COLUMBIA',
        ' OPTION III ': 'HAWAII',
        ' OPTION IV ': 'IRELAND'
    })

