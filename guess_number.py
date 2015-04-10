# GUESS THE NUMBER  
# User continually guesses until random number is guessed.

import random
numGuesses = 0

def guessNumber():
    while True:
        try:
            number = int(input('Please enter a number between 1 and 50: '))
        except ValueError:
            print('You did not enter a number.  Try again. ')
        else:
            if 1 <= number <= 50:
                break
            else:
                print('You did not enter a number in range.  Try again. ')
    print('You have entered: ', int(number))
    return number

def compNumber():
    number = random.randrange(1,51)
    return number
    
def compareNumber(comp, player):
    if player < comp:
        print('Your guess is too low.  Try again. ')
        print()
    if player > comp:
        print('Your guess is too high.  Try again. ')
        print()
    
comp = compNumber()
while True:
    player = guessNumber()
    compareNumber(comp, player)
    numGuesses += 1
    if comp == player:
        print('You guessed the correct number!  It was %s!' % (comp))
        print('You got the answer in', numGuesses, 'guesses.')
        break

    
