x = lambda x, b: x * b
print(x(2, 6))


def decrement(liss):
    return map(lambda l: l - 1, liss)


print(list(decrement([2, 4, 6, 88, 8])))


def flr(liss):
    return filter(lambda l: l % 3 == 0, liss)


print(list(flr([3, 6, 9, 1, 5])))

users = [{'username': 'Samuel', 'tweets': ['cats are funny', 'i like pie'], 'count': 23},
         {'username': 'Max', 'tweets': []},
         {'username': 'Sophie', 'tweets': ['i like pie']},
         {'username': 'Jeb', 'tweets': []}]
# inactive=list(map(lambda usr: usr['username'], filter(lambda u: len(u['username'])== 'username'.capitalize() ,users)))
# print(inactive)
# inactive = list(filter(lambda u: not u['tweets'], users))
# print(inactive)
print(sorted(users, key=lambda u: u['username']))
print(max(users, key=lambda u: u['tweets']))


def remove_negatives(lisst):
    return list(filter(lambda n: n < 1, lisst))


print(remove_negatives([-1, -6, 4, 6, 0]))


def is_all_strings(string):
    result = all(type(i) == str for i in string)
    return result


print(is_all_strings(['abcd', 1]))

# get the max or min from a list
names=['mako','ola', 'cristina']
print(max(len(name)for name in names)) #gives a number
result= max(names, key=lambda n:len(n))
print(result)

