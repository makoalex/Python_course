# write a function that takes in a string and reverses it
def reverse_string(somethin):
    return somethin[::-1]


print(reverse_string('mako'))


# II. checking if all the values in a list are a list

def list_check(lists):
   return all(type(e) for e in lists if list in lists)


print(list_check([[1,2],[1,2]]))


# function that removes very second value from a list
def remove_every_other(string):
    if len(string) > 1:
        return string[::2]
    return string


print(remove_every_other([1, 2, 3, 4, 5, 6, 7]))
