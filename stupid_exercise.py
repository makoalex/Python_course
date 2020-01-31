# greatest magnitude exercise


def greatest_magnitude(numbers):
    ret = max(abs(val) for val in numbers)
    return ret


print(greatest_magnitude([1, 5, 7, 24]))


# the sum of all the even values

def sum_even_values(*args):
    return sum(char for char in args if char %2==0)

print(sum_even_values(1,4,6,7))

# the sum of all the parameters that are floats
def sum_floats(*args):
    return sum(char for char in args if isinstance(char, float))
print(sum_floats(1.5,1.6, 5,6))

#zip function
def interleave(string1, string2):
  res=list(zip(string1, string2))
  res1=list(map(''.join, res))
  for word in res1:
      return ''.join(res1)
print(interleave('hi','yo'))

# filter funtion
def triple_and_filter(*args):
     return list(map(lambda x: x*2, filter(lambda n:n %4==0,  args)))


print(triple_and_filter(1, 2 , 3, 4 ))

# extract full name
def exttract_full_name(*dictionary):
    return list(map(lambda v: ''.join(v['first'] and v['second']), dictionary))
   # return  list(map(lambda v: '{} {}'.format(v['first'], v['second']),dictionary))

print(exttract_full_name({'first':'mako', 'second':'chan'}, {'first':'ollie','second':'coolie'}))