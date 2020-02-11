# first case when we get the information into a list
from csv import reader

with open('Tekken_fighters.csv') as file:
    csv_reader = reader(file)
    next(csv_reader)
    # we have to iterate over the  file in order to get the response
    """for row in csv_reader
        print(row)"""
    for fighter in csv_reader: """ extracting info from the list"""
    print('{} is specialised in {}'.format(fighter[0], fighter[2]))
# we can also get the CSV file as on already ordered dictionary
from csv import DictReader

# we use the same procedure as above
with open('Tekken_fighters.csv') as new_file:
    scv_reader = DictReader(new_file)
    for row in scv_reader:
        print(row)