
# if elif exercise

n = int(input().strip())
if n % 2 == 1:
    print('Weird')
elif 2 < n < 5 and n % 2 == 0:
    print('Not wer')
elif 6 < n <= 20 and n % 2 == 0:
    print('weird')
else:
    print('nnot weird')

# Read two integers The first line contains the sum of the two numbers.The second is the diff ,The third is the product.
a = int(input('enter a number'))
b = int(input('enter another number'))
if 1 <= a < 10 * 10 and 1 <= b < 10 * 10:
    summ = a + b
    diff = a - b
    prod = a * b
    print(summ, diff, prod)
# division exercise
def division(a, b):
    return a//b

a = int(input('num please'))
b= int(input('new num please'))
print(division(a, b))


