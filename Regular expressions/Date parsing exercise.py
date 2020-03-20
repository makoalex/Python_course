import re


def parse_date(input):
    date_regex = re.compile(r'(0[1-9]|[12][0-9]|3[01])[/,\.](0[1-9]|1[0-2])[/,\.]([12][0-9]{3})')
    result = date_regex.search(input)
    if result:
        my_dict= {'d':result.group(1), 'm':result.group(2), 'y':result.group(3)}
        return my_dict
    return None

print(parse_date('01/02/1999'))