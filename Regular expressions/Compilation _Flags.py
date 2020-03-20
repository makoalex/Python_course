import re

"""
Python has little preferences that we an set when compiling regular expressions
"""
# I VERBOSE
""" 
allows us to put regular expressions on multiple lines and add comments
making it easier to read
"""
pattern = re.compile(r"""
     ^([a-z0-9_\._]+)    #first part of an email
     @                  # one @ sign
     ([a-z0-9\.-]+)      # email provider
     \.                 # dot
     ([a-z\.]{2,6})$    # com, net, org etc
""", re.VERBOSE | re.IGNORECASE)

"""
 we can also insert an IGNORE CASE  which will replce the need to write upper letter characters in the REGEX
it can be written on its own as re. IGNROECASE or re.I
or it can be inserted next to the re.VERBOSE (RE.X- from extended) with an or bar (|)
"""
match = pattern.search('Ame12_4@yahoo.com')
print(match.group())
print(match.groups())
