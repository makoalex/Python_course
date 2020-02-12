# based on the tekken fighetrs csv file

from csv import DictWriter, DictReader, reader


def kg_2_pounds(kg):
    return float(kg) * 2.20


with open('Tekken_fighters.csv') as file:
    cs_readder = reader(file)
    next(cs_readder)
    conv = list(cs_readder)

with open('pound_conv.csv', 'a', newline="") as file:
    headers = ['Name', 'Country', 'Fighting style', 'Weight']
    dic_make = DictWriter(file, fieldnames=headers)
    dic_make.writeheader()
    for el in conv:
        dic_make.writerow({
            'Name': el[0],
            'Country': el[1],
            'Fighting style': el[2],
            'Weight': kg_2_pounds(el[3])
        })



#
# with open('Tekken_fighters.csv') as file:
#     new_file = DictReader(file)
#     result = list(new_file)
#
# with open('pounds_conv.csv', 'w') as file:
#     headers = ['Name', 'Country', 'Fighting style', 'Weight']
#     new_csv_file = DictWriter(file, fieldnames=headers)
#     new_csv_file.writeheader()
#     for el in result:
#         new_csv_file.writerow({
#             'Name': el['Name'],
#             'Country': el['Country'],
#             'Fighting style': el['Fighting style'],
#             'Weight': kg_2_pounds(el['Weight'])
#         })