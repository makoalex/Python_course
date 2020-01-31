
from random import choice
player_wins=0
computer_wins=0




while True:

    print("WELCOME TO THE GAME")
    print("Please enter your name player")

    user = input().strip().lower()
    print('Score:{}:{} vs computer  {} '.format(user, player_wins,computer_wins))
    print("Pick your poison: Rock, Paper, or Scissors!")
    user_inp = input().strip().lower()
    print("Hmm, {} this time, let's see what the computer picks".format(user_inp))
    computer_inp = choice(['rock', 'paper', 'scissors'])
    print(computer_inp)

    if user_inp==computer_inp:
            print("it's a tie!")
    elif user_inp == 'rock':
        if computer_inp == 'paper':
            print('Computer wins!')
            computer_wins= computer_wins+1
    elif user_inp=='rock':
        if computer_inp== 'scissors':
            print('{} wins'.format(user))
            player_wins= player_wins+1
    elif user_inp=='paper':
        if computer_inp== 'rock':
            print('{} wins!'.format(user))
            player_wins= player_wins+1
    elif user_inp== 'paper':
        if computer_inp== 'scissors':
            print('Computer wins')
            computer_wins= computer_wins+1
    elif user_inp =='scissors':
        if computer_inp == 'paper':
            print('{} wins'.format(user))
            player_wins=player_wins+1
    elif user_inp== 'scissors':
        if computer_inp== 'rock':
            print('computer takes this one!')
            computer_wins= computer_wins+1
    elif user_inp== computer_inp:
            print("it's a tie!")

    else:
        print('Wrong input! Try again you pathetic excuse for a human')


num





