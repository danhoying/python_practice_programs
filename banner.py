# BANNER
# Prints a cool banner along with an input name

def enterName():
	while True:
		name = input('Please enter your name: ')
		if not name.strip().replace(' ','',1).isalpha(): # Test for only alpha characters, allow spaces
			print('You did not enter letters only.  Try again. ')
		else:
			return name

def banner(name):
	asterisk = '*' * (len(name) + 8) # Account for the banner characters
	print(asterisk)
	print('.::', name,'::.')
	print(asterisk)
	
name = enterName()
banner(name)