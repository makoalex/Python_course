from random import choice
from csv import reader

# class Question:
#     def __init__(self, question):
#         self.question = question
#
#     def __repr__(self):
#         return "Green is a versatile word: it can be a noun, adjective, or verb;\n" \
#                " we earn greenbacks to buy greens in the market \n" \
#                "(locally sourced and organic, of course, to be as green as we can be)\nOh yeah, and it's a color too."

def ask_question():
    with open('quiz.csv', 'r') as file:
        csv_file = reader(file)
        for row in csv_file:
            print(row[0 ])

ask_question()