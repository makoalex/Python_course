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
print(extract_all_phone('hi snew number is  451 3117-231 and 465 8973-323'))
