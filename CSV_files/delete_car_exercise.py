from csv import reader, writer

def delete_cars(old_make, old_model, old_year):
    with open('cars.csv') as file:
        the_file = reader(file)
        rows= list(the_file)
        print(rows)

    with open('cars.csv', 'w', newline="") as writefile:
        new = writer(writefile)
        index = 0
        for el in rows:
            if el[0] == old_make or el[1] == old_model or el[2] == old_year:
                index = index + 1
            else:
                new.writerow(el)


print(delete_cars('Tesla', 'L4', 2019))