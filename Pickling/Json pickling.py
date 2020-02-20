# Json provides functions to encode and decode Python to Json
import json
from dictionary  import inventory
j = json.dumps(inventory )
k = json.dumps(['bar', None, 1.21,(' mickey', ' minnie') ])
print(k)
""" json. dumps formats an object of python as a string of json. there are no tuples, NONE is replaced by null"""
print(j)

import jsonpickle

class Cake:
    def __init__(self, feeling):
        self.feeling  = feeling
    def make_cake(self):
        return' the cake is ready!'
#pavlova = Cake('awsome')
"""frozen = jsonpickle.encode(pavlova)"""
""" we can store the encode method seen sbove in a file and have more flexibility"""
# with open('cake.json', 'w') as file:
#     frozen = jsonpickle.encode(pavlova)
#     file.write(frozen) # now we have a new file created
"""we can go the opposite direction now open the file in read mode, read it and uncoode it"""
with open('cake.json', 'r') as file:
    content = file.read()
    unfrozen = jsonpickle.decode(content) # it reconstructed the cat. took the json fle and reconstructed the cat object
    print(unfrozen)
    print(unfrozen.make_cake)