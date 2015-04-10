# Bagels

import random

def secretNumber(digits):
	number = list(range(10))
	random.shuffle(number)
	secretNumber = ''
	for i in range(digits):
		secretNumber += str(number[i])
	return secretNumber

def getInput(digits):
	while True:
		print('Please enter a unique', digits, 'digit number: ')
		guess = input()
		for i in guess:
			if i not in '0 1 2 3 4 5 6 7 8 9'.split():
				guess = 'no'
		if len(guess) != digits:
			guess = 'no'
		else:
			return guess

def showHints(guessed, secret, digits):
	clue = []
	for i in range(digits):
		if guessed[i] == secret[i]:
			clue.append('fermi')
		elif guessed[i] in secret:
			clue.append('pico')
	if len(clue) == 0:
		clue.append('bagels')
	totalClue = ' '.join(clue)
	return totalClue

guesses = 10
digits = 3

print('I am thinking of a', digits, 'digit number.')
print('Try to guess it!  Here are some clues...')
print()
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')
print()
secretNum = secretNumber(digits)

while True:
	entryNum = getInput(digits)
	clue = showHints(secretNum, entryNum, digits)
	print(clue)
	guesses -= 1
	print('Guesses left: ', guesses)
	print()
	if entryNum == secretNum:
		print('You got it!')
		break
	elif guesses == 0:
		print('You ran out of guesses.  The number was %s. Game over.' % secretNum)
		break
