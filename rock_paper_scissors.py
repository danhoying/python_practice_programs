#Rock Paper Scissors

import random
rock = 1
paper = 2
scissors = 3
score = 0
choice = 0
compScore = 0

while score or compScore < 6: # Play 5 rounds
	if score == 5:
		print()
		print('You scored 5 points.  You win this round!')
		break
	elif compScore == 5:
		print()
		print('The computer scored 5 points first.  You lose this round.')
		break
	while choice != 1 or 2 or 3: # Loop input text until choice is a valid attack
		choice = input('Which will you attack with: rock, paper, or scissors? ')
		if choice == 'rock':
			choice = rock
			print()
			print('Your choice: rock')
			break
		elif choice == 'paper':
			choice = paper
			print()
			print('Your choice: paper')
			break
		elif choice == 'scissors':
			choice = scissors
			print()
			print('Your choice: scissors')
			break
		
	comp = random.randrange(1,4) # Computer chooses a random number 1-3
	if comp == 1:
		comp = rock
		print('Computer: rock')
		print()
	elif comp == 2:
		comp = paper
		print('Computer: paper')
		print()
	elif comp == 3:
		comp = scissors
		print('Computer: scissors')
		print()
		
# Compare computer choice to player's input choice.  Prints appropriate text and current score

	if comp == 1 and choice == 1:
		print('The computer also chose rock.  It is a tie!')
		print('Your Score:', score)
		print('Computer Score:', compScore)
		print()
	elif comp == 2 and choice == 2:
		print('The computer also chose paper.  It is a tie!')
		print('Your Score:', score)
		print('Computer Score:', compScore)
		print()
	elif comp == 3 and choice == 3:
		print('The computer also chose scissors.  It is a tie!')
		print('Your Score:', score)
		print('Computer Score:', compScore)
		print()
	elif comp == 1 and choice == 2:
		print('Paper beats rock.  You win!')
		score += 1
		print('Your Score:', score)
		print('Computer Score:', compScore)
		print()
	elif comp == 1 and choice == 3:
		print('Rock beats scissors.  You lose.')
		compScore += 1
		print('Your Score:', score)
		print('Computer Score:', compScore)
		print()
	elif comp == 2 and choice == 1:
		print('Paper beats rock.  You lose.')
		compScore += 1
		print('Your Score:', score)
		print('Computer Score:', compScore)
		print()
	elif comp == 2 and choice == 3:
		print('Scissors beats paper.  You win!')
		score += 1
		print('Your Score:', score)
		print('Computer Score:', compScore)
		print()
	elif comp == 3 and choice == 1:
		print('Rock beats Scissors.  You win!')
		score += 1
		print('Your Score:', score)
		print('Computer Score:', compScore)
		print()
	elif comp == 3 and choice == 2:
		print('Scissors beats paper.  You lose.')
		compScore += 1
		print('Your Score:', score)
		print('Computer Score:', compScore)
		print()