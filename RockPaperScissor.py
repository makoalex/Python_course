
from random import choice


print('WELCOME TO THE GAME!!')
print('Please enter your name')
user1=input()
print('What is your choice {}:rock, paper, or scissors?'.format(user1))

user1=input().strip().lower()
computer=choice(['rock', 'paper', 'scissors'])
print(computer)

if user1==computer:
    print("It's a tie! Try again")
elif user1=='rock':
    if computer=='paper':
        print('Computer wins')
    elif computer== 'scissors':
        print('User1 wins!')
elif user1=='scissors':
    if computer=='paper':
        print('user1 wins')
    elif computer=='rock':
        print('Computer wins!')
elif user1=='paper':
    if computer=='scissors':
        print('Computer wins!')
    elif computer=='rock':
        print('User1 wins')
else:
    print('Wrong input. Try again')

