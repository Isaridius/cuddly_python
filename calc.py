

x = int(input("Enter #1:"))
y = int(input("Enter #2:"))

# User choosing a desired operation
print('''Please choose one of the following possible operations:
- 1. Add
- 2. Subtract
- 3. Multiply
- 4. Divide
''')

choice = None
while True:
    choice = input("Option chosen: ")
    choice = choice.lower()
    
    if choice not in {'add', 'subtract', 'multiply', 'divide'}:
        print("Invalid option, please choose again.")
    else:
        print(f"Operation {choice} was chosen.")
        break
# end of desired operation handling

# Numeric Inputs Only
number1 = None
while True:
    try:
        user_input = input("Enter number 1:")
        number1 = float(user_input)
        print(f"First Input: {number1}")
        break
    except ValueError:
        print(f"{user_input} cannot be converted to a floating point value")        



#add = x + y
#subtract = x - y
#multiply = x * y
#divide = x / y

#print(f"{x} + {y} = {add}")
#print(f"{x} - {y} = {subtract}")
#print(f"{x} * {y} = {multiply}")
#print(f"{x} / {y} = {divide}")