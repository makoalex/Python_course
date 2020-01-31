# # # first function
# # def say(name):
# #     print('hi, i am' + ' ' + name)
# #
# #
# # say('mako')
# #
# #
# # def sing(name):
# #     print('happy birthday to you\n ' * 3 + ' ' + name)
# #
# #
# # sing('mako')
# # flip function
# from random import choice
#
# flip = choice(['heads', 'tails', "didn't catch it"])
#
#
# def coin_flip():
#     return flip
#
#
# flip_ch = coin_flip()
# print(flip_ch)
#
# # even numbers function
#
# def make_evans():
#
#          return [num for num in range(1,50)if num%2==0]
# print(make_evans())
#
# def yell(slogan):
#
#     return slo0gan.upper()
# print(yell('leave me alone'))
#
#
def speak(animal='dog'):
    if animal == 'pig':

        return 'oink'
    elif animal == 'duck':

        return 'quack'
    elif animal == 'cat':

        return 'meow'
    elif animal == 'dog':

        return 'woof'
    else:
        return '?'


print(speak('duck'))
print(speak())
print(speak('goose'))


def test(x, z):
    return x + z


def power(num, exponent=2):
    return num ** exponent


def test2(x, z, fn):
    return fn(x, z)


print(test(2, 4))
print(test2(3, 4, power))


# returns the day and number  of the week


def return_day(num):
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satruday']
    for n in range(8):
        if num > 0 and num <= 7:
            return week[num - 1]
        else:
            return None


print(return_day(1))


# gives last element

# def last_element(a_list):
#     if a_list:
#         return a_list.pop()
#     else:
#         return None
#
#
# print(last_element([1, 2, 4]))

# print(last_element([]))

def intersection(l1, l2):
    return [val for val in l1 if val in l2]


print(intersection([1, 3, 5, 9], [1, 9, 7, 2]))


# def contains_purple(*args):
#     for word in args:
#         if 'purple' in args:
#             return True
#     return False
# print(contains_purple('red', 'mother', 'purple'))
# print(contains_purple('red', 'dawn'))

# ORDER OF PARAMETERS
def define(word, symbol, *list, name='linguistics', **kwargs):
    return word, symbol, list, name, kwargs


print(define('lingua franca ', '¤', 1, 3, 4, name='linguistics', latin='classical', greek='neoclassical'))
print(type(list))

# def order(sentence):
#
#     for num in str(len(sentence)):
#         for word in sentence:
#             if num  <=1:
#                 return word
#
# print(order( "4of Fo1r pe6ople g3ood th5e the2"))


x=lambda n: n**4
print(x(8))



def decrement(lisst):
    return list(map(lambda num:num-1, lisst))
print(decrement([6,8]))


names = ['Austin', 'penny', 'Angel', 'tommy', 'Anna']
aname= list(filter(lambda w: w[0]=='a'.upper(), names))
print(aname)

#
# name=map(lambda key: key['username'], users)
# print(name)


names= ['lassie','james','monica', 'mako alex']
assign= list(map(lambda n: '{} is your cousin'.format(n), filter(lambda val: len(val) < 5,names ) ))
print(assign)

