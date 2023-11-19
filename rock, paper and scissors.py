
# A rock-paper-scissors project.
# It is a two out of three sets of match.
# If you wanna play, type in 'rps()' in the Console.

import time
import random

def guess_number():

    computer = random.randint(1, 10)
    count = 0
    print('Guess from one to ten')
    
    while True:
        player = int(input('What is your guess?'))
        
        if player > computer:
            count += 1
            print('Too high!')
            print('You guess the number in', count, 'guesses')
        elif player < computer:
            count += 1
            print('Too low!')
            print('You guess the number in', count, 'guesses')
        elif player == computer:
            count += 1
            print('Correct.')
            break
        elif count == 9:
            print('Boom! You perfectly avoid all possibilities.')
            print( 'The correct answer is:', computer)
            break
            
    if count == 1:
        print('Lady Luck is at your side!')
    elif count <= 3:
        print('After all, we are not god, right?')
    else:
        print('You wanna try again?')
        
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
        time.sleep(1)
        
"""
    Below is the game part.
    You need to type rps() in the console!
"""      
def rps():
    print('To win the perfect ending, the possibility is 6.7%')
    count_player = 0
    count_computer = 0
    i = 0
    print('Type rock, paper or scissors')
    
    while True:
        i += 1
        print('round', i)
        computer = random.choice(['rock', 'paper', 'scissors'])
        global countdown
        countdown(3)
        if count_player == 2:
            print('\033[31m' + 'You win!' + '\033[0m')
            break
        elif count_computer == 2:
            print('\033[31m' + 'You lose!' + '\033[0m')
            break
        
        player = input('Your choice: ')
        if player == 'rock' and computer == 'paper':
            count_computer += 1
            print('lose')
        elif player == 'paper' and computer == 'rock':
            count_player += 1
            print('win')
        elif player == 'rock' and computer == 'scissors':
            count_player += 1
            print('win')
        elif player == 'scissors' and computer == 'rock':
            count_computer += 1
            print('lose')
        elif player == 'scissors' and computer == 'paper':
            count_player += 1
            print('win')
        elif player == 'paper' and computer == 'scissors':
            count_computer += 1
            print('lose')
        elif player == computer:
            print('Again')
                            
    if count_player == 2:       
        print('You wanna beat me further?')
        output = guess_number()
        countdown = 5
        if output == 'Lady Luck is at your side!':
            print('PERFECT ENDING\n' * 5)
        elif output == 'After all, we are not god, right?':
            print('You wanna try again?')
        else:
            while countdown > 0:
                print('There is {} seconds left'.format(countdown))
                time.sleep(1)
                countdown -= 1
            print('\033[31m' + 'Time is out! You LOSE!' + '\033[0m')
            print('BAD ENDING')
            
            
            
        
        


    