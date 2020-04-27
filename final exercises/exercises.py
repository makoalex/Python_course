# # write a function that takes in a string and reverses it
# def reverse_string(somethin):
#     return somethin[::-1]
#
#
# print(reverse_string('mako'))
#
#
# # II. checking if all the values in a list are a list
#
# def list_check(lists):
#     return all(type(e) for e in lists if list in lists)
#
#
# print(list_check([[1, 2], [1, 2]]))
#
#
# # function that removes very second value from a list
# def remove_every_other(string):
#     if len(string) > 1:
#         return string[::4]
#     return string
#
#
# print(remove_every_other([1, 2, 3, 4, 5, 6, 7]))
#
#
# # III. function that returns a dictionary with the keys as the vowels
# def vowel_count(word):
#     return {k: word.lower().count(k) for k in word if k in 'aeiou'}
#
#
# (vowel_count('Elie'))
# """IV. function that takes a list and a number and returns  the 1st pair of numbers that sum to the number passed"""
# def sum_pairs(pairs, num):
#     return [i for i in pairs if num-i in pairs ]
#
#
#
# print(sum_pairs([1,2,4,3],5))


def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 2:
        return '{} and {} like this'.format(names[0], names[-1])
    elif len(names) == 3:
        return '{}, {}, and {} like this'.format(names[0], names[1], names[2])
    elif len(names) == 1:
        return '{} likes this'.format(names[0])
    elif len(names) > 3:
        return '{}, {}, and {} others like this'.format(names[0], names[1], len(names) - 2)


print(likes(['john', 'jack', 'alex', 'annie', 'sam', 'gertrude']))


# Given two arrays a and b write a function comp(a, b)
# (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities.


def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


print(comp([121, 144, 19, 161, 19, 144, 19, 11], [100, 14641, 20736, 361, 25921, 361, 20736, 361]))


# a program that among the given numbers finds one that is different in evenness, and return a position of this number.
def iq_test(numbers):
    num = [int(n) % 2 == 0 for n in numbers.split()]
    print(num)
    if num.count(True) == 1:
        result = num.index(True) + 1
        return result
    elif num.count(False) == 1:
        res = num.index(False) + 1
        return res


print(iq_test("1 4 3 5"))
