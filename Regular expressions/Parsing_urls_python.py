import re

url_regex = re.compile(r'https?://www\.[A-za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*')
match = url_regex.search('https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/9328506#questions')
print(match.group())

""" we can also select based on groups within the link and print out only sections/portions of it
"""
url = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
result = url.search('https://www.stackoverflow.com/questions/161738/what-is-the-best-regular-expression-to-check-if-a-string-is-a-valid-url/20542241#20542241')
print(result.groups())
print(result.group(0))
""" with regex the index 0 will not return the 1st element as with slices,
but rather return the same as group() the whole url"""
print(result.group(1))
print(result.group(2))
print(result.group(3))
""" wecan pretty print it as well with an f string"""
print('PROTOCOL: {}'.format(result.group(1)))
print('DOMAIN: {}'.format(result.group(2)));
print('THE REST : {}'.format(result.group(3)))
