# write a function that takes in a first and last name and adds it to a new file
from csv import reader, writer, DictReader


def add_user(first_name, last_name, country, style, weight):
    return first_name, last_name, country, style, weight


with open('Tekken_fighters.csv', 'a', newline="") as file:
    open_file = writer(file)
    open_file.writerow(add_user('claudio', 'Serafino', 'Italy', 'sirius', 87))

# printing all the first and last names from the tekken fighters file


