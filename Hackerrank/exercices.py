#
# # if elif exercise
#
# n = int(input().strip())
# if n % 2 == 1:
#     print('Weird')
# elif 2 < n < 5 and n % 2 == 0:
#     print('Not wer')
# elif 6 < n <= 20 and n % 2 == 0:
#     print('weird')
# else:
#     print('nnot weird')
#
# # Read two integers The first line contains the sum of the two numbers.The second is the diff ,The third is the product.
# a = int(input('enter a number'))
# b = int(input('enter another number'))
# if 1 <= a < 10 * 10 and 1 <= b < 10 * 10:
#     summ = a + b
#     diff = a - b
#     prod = a * b
#     print(summ, diff, prod)
# # division exercise
# a = int(input('num'))
# b = int(input('num 2'))
# print(a//b)
# print(a/b)

#Read an integer . For all non-negative integers , print . See the sample for details.


i = 0
N = int (input('number'))
while 1 < N <= 21 and i < N:
    print(i * i)
    i = i + 1

