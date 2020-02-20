# Json provides functions to encode and decode Python to Json
import json
from dictionary  import inventory
j = json.dumps(inventory )
print(j)
