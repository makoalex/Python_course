from csv import reader, writer


# #
def update_cars(old_make, old_model, old_year, new_make, new_model, new_year):


    with open('cars.csv') as file:
        new_fil = reader(file)
        rows = list(new_fil)
        print(rows.)
        with open('cars.csv', 'w') as file:
            new = reader(file)
            new_one = 0
            for row in rows:
                for el in row:
                    if el == old_make == old_model == old_year:
                        new_el = new_make, new_model, new_year
                        return new_el

print(update_cars('Ford', 'Mustang', 2008, 'Tesla', 'L4', 2019))
