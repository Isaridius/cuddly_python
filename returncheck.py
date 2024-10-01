def add_and_print(a, b):
    print(a + b)  # This will just show the result on the console.

def add_and_return(a, b):
    return a + b  # This returns the result, allowing you to reuse it.

# Using print
add_and_print(3, 4)  # prints: 7
result = add_and_print(3, 4)  # prints: 7, but result will be None because nothing is returned

# Using return
result = add_and_return(3, 4)  # No print, but result holds the value 7
print(result)  # prints: 7
