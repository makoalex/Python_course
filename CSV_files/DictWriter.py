# another way of writing data using DICTWRITER
# creates a writer objrct for writing using dictionaries
# it can me a bit more verbose than the WRITER VERSION
from csv import DictWriter

"""we're going to add to the tekken file using dictwriter"""

with open("Tekken_fighters.csv", 'a', newline="") as file:
    headers = ['Name', 'Country', 'Fighting style']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        'Name': "Alisa Bosconovitch",
        'Country': 'Russia',
        'Fighting style': "Unique"
    })
