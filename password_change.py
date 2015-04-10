# PASSWORD CHANGE
# Changes an existing password

print('Old password is "HelloWorld" for testing purposes')
print()

old_password = 'HelloWorld'
old_check = ''

def passwordChange(old_password, old_check):
    while True:
        while old_check != old_password:
            old_check = input('Please enter your old password: ')
            if old_check != old_password:
                print('That is not your old password.')
        new_pass1 = input('Enter your new password: ')
        new_pass2 = input('Re-enter your new password: ')
        if new_pass1 != new_pass2:
            print('Your passwords don\'t match.')
        elif new_pass1 and new_pass2 == old_password:
            print('That is your old password.')
        elif new_pass1.lower() == new_pass1:
            print('Your password must contain an upper-case letter.')
        elif new_pass2.lower() == new_pass2:
            print('Your password must contain an upper-case letter.')
        elif new_pass1.upper() == new_pass1:
            print('Your password must contain a lower-case letter.')
        elif new_pass2.upper() == new_pass2:
            print('Your password must contain a lower-case letter.')
        elif len(new_pass1) and len(new_pass2) <= 7:
            print('Your password needs to be at least 8 characters long.')
        else:
            print('Your password has been changed.')
            return new_pass2
            
passwordChange(old_password, old_check)
    
