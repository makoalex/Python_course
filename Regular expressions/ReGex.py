# importing regex module
import re

# define our regex phone number
pattern = re.compile(r'\d{3} \d{4}-\d{3}')
"""
we only need to compile once
if we run help on pattern we will see that is a compiled regular expressions object
that has a bunch of methods 
"""
# search a string with our regex
"""search can however return only one matching result 
"""
res = pattern.search(' call me at this number 987 4721-211')
"""we have to call res.group () a method in order to get the result 
otherwise we get a match object"""
print(res.group())
result = pattern.findall(' call me on 987 4721-211 or if you can not reach me try 965 4512-312')
""" find all will print all matches"""
print(result)
""" we can also skip the compiling, if we use re.search(pattern, string, flags=0) instead of 
Pattern.search(string[, pos[, endpos]])"""
pat = re.search(r'\d{3} \d{4}-\d{3}', ' call me at this number 987 4721-211')
print(pat.group())

