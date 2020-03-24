import sqlite3

# creating connection
connection = sqlite3.connect("chocolate.db")
c = connection.cursor()
# we can insert into Python using the sql method, which is a bit redundant
"""insert = "INSERT INTO chocolates values ('Lindor', 'Switzerland,EU'," \
         " 'Lindt& Sprungli');
# we execute the  new code
c.execute(insert)
# we commit and save the changes
connection.commit()
# close
connection.close()"""
""" we can add things manually, but it's not recommended nor PYTHONIC """
# we know we have certain variables that we can insert manually for example through format method
# DON'T DO IT!!!
# var_from_form = 'Lion Bar'
# insert1 = "INSERT INTO chocolates (name) VALUES ('{}')".format(var_from_form)
# c.execute(insert1)
# connection.commit()
# connection.close()

