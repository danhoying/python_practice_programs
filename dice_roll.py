# Dice Rolling Simulator

import random

def rollAgain():
    # This function returns True if the player wants to roll again, otherwise it returns False.
    print('Do you want to roll again? (yes or no)')
    return input().lower().startswith('y') 
    
while True:
    try:
        numSides = int(input('This program will roll a die.  Choose the number of sides your die will have: '))
    except ValueError:
        print('You did not enter a number.  Try again. ') # Keeps asking for input if player enters a non-number
    else: 
        break # player entered a number
print('Okay, a', numSides, '- sided die ')
print()

number = random.randrange(1, int(numSides) + 1)
print('The dice roll result is: ', number)
print()

while rollAgain():
    while True:
        try:
            numSides = int(input('This program will roll a die.  Choose the number of sides your die will have: '))
        except ValueError:
            print('You did not enter a number.  Try again. ') # Keeps asking for input if player enters a non-number
        else: 
            break # player entered a number
    print('Okay, a', numSides, '- sided die ')
    print()
    
    number = random.randrange(1, int(numSides) + 1)
    print('The dice roll result is: ', number)
    print()

        
    
    
