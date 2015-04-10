# HANGMAN
# Player guesses individual letters to try to get the secret word.
# Default guesses = 8

import random
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

guessed = ''
guesses = 0
correct_letters = ''
missed_letters = ''
game_is_done = False

def getWord(): # Chooses random word from list
    word = random.choice(words)
    return word

secret_word = getWord()
print('Welcome to Hangman. Try to guess the secret', len(secret_word), '- letter word!')
print('Hint: it\'s an animal.')

def getGuess(already_guessed): # Get the user's letter guess
    while True:
        guess = input('Please enter a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('You have not entered a letter. Try again')
        elif guess in already_guessed:
            print('You have already guessed that letter')
        else:
            return guess

def fillBlanks(secret_word, guess): # Fill blanks in secret word if correct letter is guessed
    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in guess:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end='')

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y') 

while True: # Remember to link this to incrementing guesses 
    print()
    print('Letters you have missed: ', missed_letters)
    print('Guesses left: ', 8 - guesses) # Change guesses here
    print()  

    guess = getGuess(missed_letters + correct_letters)
    guessed = guessed + guess
    fillBlanks(secret_word, guessed)
    
    if guess in secret_word:
        correct_letters = correct_letters + guess
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print()
            print('You have won! The secret word was', secret_word) 
            game_is_done = True           
    else:
        missed_letters = missed_letters + guess
        guesses += 1
        if guesses == 8: # Change guesses here
            print()
            print('Sorry, you have run out of guesses. The secret word was', secret_word)
            game_is_done = True

    if game_is_done:
        if playAgain():
            print()
            guessed = ''
            guesses = 0
            correct_letters = ''
            missed_letters = ''
            game_is_done = False
            secret_word = getWord()
            print('Welcome to Hangman. Try to guess the secret', len(secret_word), '- letter word!')
            print('Hint: it\'s an animal.')
        else:
            break
