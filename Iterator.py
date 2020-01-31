# the for loop runs ITER in the background making the object an iterator after which it calls next
# on every single item making the object an iterable

def my_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            it = next(iterator)
            print(it)
        except StopIteration:
            print('end')
            break


my_loop('pup')


def new(iterable, func):
    result = iter(iterable)
    while True:
        try:
            new_iter = next(result)
        except StopIteration:
            break
        else:
            func(new_iter)


def add(i):
    print(i + 2)


print(new([1, 4, 5], add))


# GENERATORS HELP CREATE ITERATORS. Every gnerator is an iterator bu not every iterator is a generator.
# they are functions that use YIELD instead of return
# generator functions return a generator, generators are iterators

def week():
    week_day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for day in week_day:
        yield day


weekly = week()
print(next(weekly))
print(next(weekly))
print('me')
for day in weekly:
    print(day)


def yes_or_no():
    answers = ('yes', 'no')
    while answers:
        for a in answers:
            yield a


# soda song

def make_song(number, drink):
    for i in range(number, -1,-1):
        if i == number:
            yield '{} bottles of {} on the wall'.format(number, drink)
        elif i < number:
            yield '{} bottles of {} on the wall'.format(i, drink)
            i = number - 1
        else:
            yield 'no more bottles of {} on the wall'.format(drink)


count = make_song(7, 'soda')
print(next(count))

def get_multiples(num=2, count=10):
    for i in range(1, count-1):
        neww= num*i
        yield neww
eve= get_multiples()
print(next(eve))

def get_unlimited_multiples(num = 2):
    new_list=[]
    for i in range (1, 29):
        if i%num==0:
            yield i
            new_list.append(i)
            
ev = get_multiples()
print(next(ev))
print(next(ev))







