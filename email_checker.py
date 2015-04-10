# E-MAIL CHECKER
# check email address for validity

def emailCheck():
	while True:
		email = input('Please enter your email address: ')
		if '@' not in email:
			print('Please enter a valid email address.')
		elif ' ' in email:
			print('Please enter a valid email address.')
		elif email.count('@') > 1:
			print('Please enter a valid email address.')
		elif email[0] == '.' and email[0] == '@':
			print('Please enter a valid email address.')
		elif email[-1] != 'm' and email[-2] != 'o' and email[-3] != 'c' and email[-4] != '.':
			print('Please enter a valid email address.')
		elif email[-1] != 't' and email[-2] != 'e' and email[-3] != 'n' and email[-4] != '.':
			print('Please enter a valid email address.')
		else:
			return email
			
emailCheck()