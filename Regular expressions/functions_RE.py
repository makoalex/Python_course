import re


# making a function that extracts a phone number and all phone numbers in a given sequence

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{4}-?\d{3}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None


def extract_all_phone(input):
    phone_reg = re.compile(r'\d{3} \d{4}-?\d{3}')
    match_all = phone_reg.findall(input)
    return match_all


print(extract_phone('new number is 451 3117-231'))
print(extract_phone(' 451 3117-231nkn'))
print(extract_all_phone('his new number is  451 3117-231 and 465 8973-323'))


# checking now if  the phone number we extracted is a valid number
def valid_phone(func):
    phone_reg = re.compile(r'\d{3} \d{4}-?\d{3}')
    match = phone_reg.fullmatch(func)
    if match:
        return True
    return False


print(valid_phone(('new number is 451 3117-231')))
print(valid_phone('451 3117-231'))

"""it can also be done with the code from the forst function by just adding ^ at the beginning of the sequence and $ at 
the end to limit where it starts end ends"""
