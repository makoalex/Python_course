import sqlite3
import collections
import re
connection = sqlite3.connect('chocolate.db')
c = connection.cursor()

choco = [
    ('Curly Wurly', 'Uk', 'Cadbury'),
    ('Daim', 'Sweden, Middle East', 'Kraft Foods'),
    ('Galaxy', 'Uk, India, Pakistan', 'Cadbury'),
    ('Intense Orange', 'Switzerland', 'Lindt & Sprungli'),
    ('Krembanan', 'Norway', 'Nidar'),
    ('Maji Almond', 'Japan', 'Meji')
]
# in order to bulk add we can use the sql way:
# but if we want to do something  with the values, this method will not allow it
c.executemany("INSERT INTO chocolates Values (?,?,?)", choco)

connection.commit()


# the other way is by iterating through
choco1 = [
    ('Milka', 'Germany, EU', 'Kraft Foods'),
    ('Old faithful', 'USA', 'Idaho, Candy Company'),
    ("Reese's Peanut Butter Cups", 'USA, Woldwide', 'Hershey'),
    ('Oh Henry', 'USA, Canada','Ferrara Hershey in Canada' )
]
for choc in choco1 :
    c.execute('INSERT INTO chocolates Values (?,?,?)', choc)
    print('Eurika')


connection.commit()
connection.close()