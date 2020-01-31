# is written to make sure that your own code works by running tests on your code
# it helps reduce bugs into existing tests
# you ensure that new code introduced doesnt break existing code or features ( for example with refactoring )
# Test driven developpemnt is the coding modality where you write the test by which the code will aby . once your code passes the feature is considered complete.


# ASSERTIONS
# makes sure that certain expression must be true,or it will throw an Assertion error
# we can add another assertion message. It can be over ridden using "-O" so it can cause problems with bigger tests.
def add_numbers(a,b):
    assert a > 0 and 1000 > b > 0, "both numbers must be bigger then 0 but b cant go over 1000"
    return a +b
0
def check_name(name):
    assert name == 'Mako'.lower(), " i only say hi to Mako"
    return 'Hi {}'.format(name)
name = input('enter a name ')
print(check_name(name))

# DOCTESTS
# are done inside the docstrings

def add(a,b):
    """
    add 2 numbers together
    >>> add(1,2)
    3
    >>> add(int, str)
    >>> add(2,4)
    Traceback (most recent call last):
        ...
    TypeError: Unsupported operand type(s) for +:'int' and 'str'

    """
    return a*b
print(add(2,4))
