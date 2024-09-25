# Goal: To create a password generator
# Requires password length
# Requires passwrod criteria
# Does it contain uppercase?
# Does it contain numbers
# Special characters? 
# Generate a password with the given constraints
# Output the password

import random

#Program Intro
print("Password Generator")

#Length
pwdLength = int(input("Enter the length of pwd: "))

lowercase = list(range(97, 123))
uppercase = list(range(65, 91))
digits = list(range(48, 57))
special = list(range(33, 48)) + list(range(58, 65)) + list(range(91,97)) + list(range(123, 126))

pwdSymbols = lowercase.copy() #list of possible characters

hasUpper = input("Include uppercase? (Y/N)")
if hasUpper == 'Y' or hasUpper == 'y':
    pwdSymbols.extend(uppercase)
    
hasSpecial = input("Include special? (Y/N)")
if hasSpecial == 'Y' or hasSpecial == 'y':
    pwdSymbols.extend(special)

hasDigits = input("Include digits? (Y/N)")
if hasDigits == 'Y' or hasDigits == 'y':
    pwdSymbols.extend(digits)


newPassword = "" #Empty string

while len(newPassword) != pwdLength:
    randomSymbol = chr(random.choice(pwdSymbols))
    newPassword = newPassword + randomSymbol
#end of while oook

print(f"{newPassword}")