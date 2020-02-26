from csv import reader, writer


# #
def update_cars(old_make, old_model, old_year, new_make, new_model, new_year):
    with open('cars.csv') as file:
        new_fil = reader(file)
        rows = list(new_fil)
        print(rows)
        with open('cars.csv', 'w') as write_file:
            new_writer = writer(write_file)
            index = 0
            for el in rows:
                if el[0] == old_make or el[1] == old_model or el[2] == old_year:
                    new_writer.writerow([new_make, new_model, new_year])
                    index +=1
                else:
                    new_writer.writerow(el)
            print('cars uppdated {}'.format(index))


print(update_cars('Ford', 'Mustang', 2008, 'Tesla', 'L4', 2019))
