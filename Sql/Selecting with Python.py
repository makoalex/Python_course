# until no we didn't get anything back when we committed into the database
# if we want to get a result back we can either iterate, or converting the data into an array or list
import sqlite3
connection = sqlite3.connect('director.db')
c = connection.cursor()
# c. execute("CREATE TABLE directors (first_name TEXT, last_name TEXT, film TEXT, country TEXT);")
#connection.commit()
query = [
    ['Alfred','Hitchcock', 'Psycho', 'UK'],
    ['Ingmar', 'Bermgan', 'Smultronstallet', 'Sweden'],
    ['Cristopher ', 'Nolan', 'Dunkirk', 'Uk'],
    ['Steven', 'Spielberg', "Schindler's List", 'USA'],
    ['Martin', 'Scorsese', 'Taxi Driver', 'USA'],
    ['Charles', 'Chaplin', 'The Great Dictator', 'Uk']
]
# for q in query:
#     c.execute('Insert into directors values (?,?,?,?)', q)
#     print('succesful')

connection.commit()
#1. we can get data by using  execute using the SELECT* and iterate
c.execute("select* from directors ")
"""for result in c:
    print(result)"""
#2. if we want them in for of a list, we can use
print(c.fetchall())
# c. execute("select * from directors where first_name ='Martin'")
# print(c.fetchone())
# c. execute("select country from directors where country is not 'USA'")
 # print(c.fetchall())
c. execute("select first_name from directors  order by last_name")
print(c.fetchall())
