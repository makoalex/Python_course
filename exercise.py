

# question = 'say something? '
# print(question)
# while True:
    #
    # answer = input()
    # if answer!='stop copying me':
    #     print(answer)
    # else:
    #     print('you win')


import random

random_num = random.randint(1, 10)


# while True:
#     request = 'Guess a number between 1 and 10 '
#     print(request)
#     user_input = int(input())
#
#     if user_input> random_num:
#         print('too high, try again')
#
#     elif user_input<random_num:
#         print('too low, try again')
#     else:
#         print('you guessed it!!')
#
#         replay=input('would you like another go?  y/n').lower().strip()
#         if replay=='y':
#             random_num = random.randint(1, 10)
#
#         else:
#             print('takk')
#             break
# list1=['you','me','us','me','ola','mako']
# print(list1.index('me'))
# print(list1.count('me'))
# list1.sort()
# print(list1)
# random=['python', 'is ', 'fun','but','a little', 'complicated']
# print(random[1:])
# print(random[:3])
# print(random[::-1])
# print(random[::1])
# random[2],random[-1]=random[-1], random[2]
# print(random)

# print([num*2for num in range(1,7,2)])
# print([bool(val) for val in ['mother',3, 0, '']])
# numb=[1,3,4,5,6,8,22]
# string=[str(num) + ' '+ 'time' for num in numb]
# print(string)
# even=[num for num in numb if num%2==0]
# other=[num/2 if num%2!=0 else num/2 for num in numb]
# print(even)
# print(other)
# words=['she is so much fun']
# word=[char for char in words if char not in 'a e i o u']
# print(word)

#list=[[1,2,3],[4,5,6],[7,8,9]]
# print(list[-2][-3])
# for num in list[0]:
#     print(num*num)
# for num in list:
#     for value in num:
#         print(value)
# board=[[num for num  in range(1,5)] for value in range(1,5)]
# print(board)
# sign=[['X' if num%2==0 else 'O' for num in range(1,5)] for val in range(1,5)]
# print(sign)
answer=[[number for number in range(10)] for rows in range(11)]
print(answer)