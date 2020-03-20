""" you can substitute a string or reference parts of capture groups"""
""" Python has also string functions that can help us sometimes work with parts of the strings
instead of using the Re module but in those cases where it would require too much iteration, we can use
SUB from re module
"""
import re

text = " Last night in an unfortunate twist of events, MR. Chow and Mrs. Jones killed Ms. Daisy the tenant"
pattern_regex = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z]+)', re.I)
result = pattern_regex.search(text)
print(result.groups())
""" if we want to substitute one of the names with a code we can use the sub """
new_result = pattern_regex.sub('Unnamed', text)
print(new_result)
"""  and we get the regular expressions filtered"""
""" we can also add groups notifications tht let us reference  our capture groups"""
new_text = 'Last night in an unfortunate twist of events, MR. Chow and Mrs. Jones killed Ms. Daisy the tenant'
text_regex = re.compile(r'(Mr\.|Mrs\.|Ms\.) [a-z][a-z]+', re.I)
"""if we want to have for example  Mr. Unnamed, Mrs. unnamed we have to writ ethe groups number in the syntax bellow"""
text_res = text_regex.sub('\g<1>Unnamed', new_text)
print(text_res)
""" if we want to get only the first letter we first have to modify the regex expression ([a-z]) [a-z]+ (first parenthesis
selects the first letter of the name ), set it into a group and call the groups number within the sub method """
first_letter = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+',re.I)
res = first_letter.sub('\g<1> \g<2>',new_text)
print(res)