import sqlite3
# open a connection to a data base
connection = sqlite3.connect("chocolate.db")
# 1.create cursor object using that connection and save it to a variable
c = connection.cursor()
# 2.execute some code with it
c.execute("CREATE TABLE chocolates (name TEXT, distribution TEXT, manufacturer TEXT);")
""" that's how to create table from python"""


# 3.commit the changes we have just made
connection.commit()
# 4. close the connection
connection.close()
