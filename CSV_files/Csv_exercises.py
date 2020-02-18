# write a function that takes in a first and last name and adds it to a new file
from csv import reader, writer, DictReader
# #
# #
# # def add_user(first_name, last_name, country, style, weight):
# #     return first_name, last_name, country, style, weight
# #
# #
# # with open('Tekken_fighters.csv', 'a', newline="") as file:
# #     open_file = writer(file)
# #     open_file.writerow(add_user('claudio', 'Serafino', 'Italy', 'sirius', 87))
# #
# # # printing all the first and last names from the tekken fighters file
# def print_users():
#
#
#     with open('Tekken_fighters.csv') as new_file:
#         scv_reader = DictReader(new_file)
#         for row in scv_reader:
#             for k, v in row.items():
#                 if k == 'Name' or k == 'Country':
#                     print('{} {}'.format(row['Name'], row['Country']))
# print(print_users())
#
# # finding an user and returning he index where the user is found
#
def find_user(Name, Country):
    with open('Tekken_fighters.csv') as file:
        new_one = reader(file)
        new_file = list(new_one)

        try:
           return new_file.index([Name, Country])
        except:
            return '{} {} not found'.format(Name, Country)


print(find_user('Nina Williams', 'Ireland'))
