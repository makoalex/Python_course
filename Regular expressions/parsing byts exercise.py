import re


def parse_bytes(string):
    bytes_regex = re.compile(r'[0-1]{8}')
    result = bytes_regex.findall(string)
    return result


print(parse_bytes('the string is 11100011 amd 10101010'))

""" we can also pass symbolic group names to each group.
the substring matched by the group is accessible via the symbolic group name"""


def name(input):
    name_regex = re.compile(r'(?P<title>Mrs\.|Ms\.) (?P<first>[a-zA-Z]+) (?P<last>[a-zA-Z]+)')
    names = name_regex.search(input)

    print(names.group('title'))
    print(names.group('first'))
    print(names.group('last'))


name(' Mrs. Marie Antoinette')
