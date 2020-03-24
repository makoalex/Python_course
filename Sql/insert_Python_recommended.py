import sqlite3

connection = sqlite3.connect("chocolate.db")
c = connection.cursor()
# we know we have data coming in but we don't know what it will contain
# for demonstration purposes we will use a variable and added to the database
data = ('Cadbury', 'Uk, Australia, New Zealand', 'Cadbury')
# the way to add to the database is to add "?" for every value that we want added in
# and execute the variable with a tuple containing the values we want to be added in:
query = " INSERT INTO chocolates VALUES (?,?,?);"
c.execute(query, (data))
connection.commit()
connection.close()
