from math import sqrt

print(sqrt(15129))

# using the keyword built in module

from keyword import iskeyword


def contains_keyword(*args):
    for i in args:
        if iskeyword(i):
            return True
    return False


print(contains_keyword('print', 'matta'))
print(pythn)
