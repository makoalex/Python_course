# writing to csv files can be done either in the form of lists or dictionaries
# USING LISTS import writer from csv and writerow

from csv import writer, reader
with open('Tekken_fighters.csv', 'w', newline="") as file:
    csv_writer = writer(file)
    csv_writer.writerow(['Name', 'Country', 'Fighting style', 'Weight'])
    csv_writer.writerow(['Jin Kazama', 'Japan', 'karate', 75])
    csv_writer.writerow(['Lee Chaolan', 'Japan', 'Martial arts', 73])
    csv_writer.writerow(['Brian Fury', 'USA', 'Kickboxing', 86])
    csv_writer.writerow(['Nina Williams', 'Ireland', 'Aikido', 54])
    csv_writer.writerow(['Katarina Alves', 'Brazil', 'Savate', 57])
with open('cars.csv', 'w') as file:
    new_file = writer(file)
    new_file.writerow(['Make', 'Model', 'Year'])
    new_file.writerow(['Hyundai', 'I30', 2017])
    new_file.writerow(['Ford', 'Mustang', 2008])

#copying the csv file into another with all uppercase
with open('Tekken_fighters.csv') as file:
    csv_reader = reader(file)
    new_csv = [[e.upper() for e in row]for row in csv_reader]
    for row in new_csv:
        print(row)

with open('Uppercase_file.csv', 'w', newline="") as file:
    csv_writer = writer(file)
    for n in new_csv:
        csv_writer.writerow(n)


