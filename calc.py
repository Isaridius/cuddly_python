# Basic Calculator v2

# Numeric Input Code held in a function
def numericInput(prompt: str) -> float:
    number1 = None
    while True:
        try:
            user_input = input(prompt)
            number1 = float(user_input)
            print(f"First Input: {number1}")
            return number1 # instead of break
        except ValueError:
            print(f"{user_input} cannot be converted to a floating point value")
# end of numericInput()

# User choosing a desired operation
print('''Please chooses the following possible operations:
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

# Using our custom numericInput Function
number1 = numericInput("Enter Number 1: ")
number2 = numericInput("Enter Number 2: ")

# Doing our desired calculation
result = None
if choice == "add":
    result = number1 + number2
elif choice == "subtract":
    result = number1 - number2
elif choice == "multiply":
    result = number1 * number2
elif choice == "divide":
    # Restrict Division by Zero
    if choice == "divide":
        try:
            result = number1 / number2
        except ZeroDivisionError:
            result = None
            print(f"Since the variable number2 is zero, there is no solution.")

# Outputting the result
if result is not None:
    print(f"The result is: {result}.")
