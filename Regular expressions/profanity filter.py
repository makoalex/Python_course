import re


def censor(input):
    string = re.compile(r'\b[f][rack]+[e-n,r]+\b', re.I)

    if string:
        result = string.sub('censored', input)
        return(result)
    return None
print(censor('you mother fracker'))

