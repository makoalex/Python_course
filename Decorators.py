# nesting a function within another function
from random import choice


def say_something(name):
    def salutation():
        message = choice(("hey there", "you're the best", 'wuv ya'))
        return message

    end_result = salutation() + ' ' + name
    return end_result


print(say_something('Ola'))


def shopping(name):
    def city():
        lis = choice(('oslo', 'bergen', 'sandefjord'))
        return 'the biggest {} is in {} '.format(name, lis)

    return city()


market = shopping('rema1000')
print(market)
print(type(market))


def polite(func):
    def pleasantries():
        func()
        print('what a pleasure to meet you')
        print('hope you have a nce day')

    return pleasantries


@polite  # or we can do rage= polite(meah) and call rage as a function in order to execute the code
def meah():
    print('i already hate you !')


@polite  # or we can do greet = polite(greet) and cal greet as a function. the name for greet can be anything else
def greet():
    print('hi my name is Mako')


meah()
greet()


def order(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).capitalize()

    return wrapper


@order
def book_name(book):
    return '{} is the book i would recommend.'.format(book)


@order
def better(book1, book2, site):
    return '{} or {}  are more popular, or better yet check {} for references'.format(book1, book2, site)


print(book_name('wutherigheights'))
print(better('animal farm', '1984', 'bookdepositoru'))

from math import sqrt


def math(fn):
    def wrapper(*args):
        return sqrt(fn(args))

    return wrapper


@math
def sum_is(*args):
    return sum(*args)


print(sum_is(60, 4))

# Example of preserving documentation

from functools import wraps


def new_func(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """TESTING THE METADATA"""
        print('you are about to call {}'.format(fn.__name__))
        print('you are about to call {} '.format(fn.__doc__))
        return fn(*args, **kwargs)

    return wrapper


@new_func
def test(a, b):
    """THIS ADDS TWO OR MORE ELEMENTS"""
    return a + b


print(test(1, 2))
print(test.__doc__)
print(test.__name__)
help(test)

# Example of time elapse

from time import time


def lapse(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print('Calculating time for {}'.format(fn.__name__))
        print('Elapsed time is: {}'.format(end - start))
        return result

    return wrapper


@lapse
def test_sum_generator():
    return sum(i for i in range(100000))


print(test_sum_generator())


@lapse
def test_sum_list():
    return sum([i for i in range(100000)])


print(test_sum_list())


# new exercise
def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print('here are the arguments: {}'.format(args))
        print('here are the keyword arguments: {}'.format(kwargs))
        return fn(*args, **kwargs)

    return wrapper


@show_args
def do_noting(*args, **kwargs):
    return args, kwargs


print(do_noting(1, 2, 3, a=7, b=8))


# new exercise

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = [fn(*args), fn(*args)]
        return result

    return wrapper


@double_return
def add(x, y):
    return x + y


print(add(1, 2))


# new cize
def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) >= 3:
            raise ValueError('Too many arguments!')
        return fn(*args, **kwargs)

    return wrapper


@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)


print(add_all(1, 2))


# new cize
def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for i in args:
            if type(i) != int:
                return 'Please only invoke with integers'
            return fn(*args, **kwargs)

    return wrapper


@only_ints
def add(x, y):
    return x + y


print(add('1', '2'))


# new cize
def ensure_authorized(funct):
    @wraps(funct)
    def wrapper(*args, **kwargs):
        for key, value in kwargs.items():
            if key == 'role' and value == 'admin':
                return funct(*args, kwargs)
            return 'Unauthorized'

    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    return 'shh! dont tel anybody'


print(show_secrets(role='admmin'))


# decorator with an argument

def test_1st_arg(value):
    def inner_funct(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                return 'The first argument needs to be {}'.format(value)
            return func(*args, **kwargs)

        return wrapper

    return inner_funct


@test_1st_arg('kål')
def list_stuff(*groceries):
    return groceries


print(list_stuff('kål', 'apples'))


# enforcing a decorator with types

def enforce_types(*types):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            arg_list = []
            for (i,j) in zip(args, types):
                arg_list.append(j(i))
            return fn(*arg_list, **kwargs)
        return wrapper
    return decorator
@enforce_types(str, int)
def count(text, time):
    for i in range(time):
        print(text)
count('cute', '5')

# decorator with  time sleep function
from time import sleep

def delay(time):
    def inner_function(fn):
        @wraps(fn)
        def wrapper_fn(*args, **kwargs):
            print('waiting {}s before running {}'.format(time, fn.__name__))
            sleep(time)

            return fn(args, kwargs)
        return wrapper_fn
    return inner_function
@delay(4)
def say_hi(*args, **kwargs):
    return 'hi'
print(say_hi('howdy'))

