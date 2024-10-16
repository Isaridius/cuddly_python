def areaCircle(radius, pi=3.14):
    ''' calculates the area of a circle
    args:
        radius : represents the radius of the circle to the floating point value
        pi : pi

    return: 
        an integer describing the radius
    '''

    area = pi * (radius ** 2)

    return area

my_radius = float(input())
pi = 3.14159

my_circle_area = areaCircle(my_radius, pi)
my_circle_area2 = areaCircle(my_radius, 3.14)

print(f'The area of my circle is {my_circle_area} units squared.')
print(f'The area of my circle with pi of 3.14 is {my_circle_area2} units squared.')















# EXAMPLE 2

x = 10

def f(x):
    # The x variable belongs to f(x)
    # This is called the local scope
    x = x + 2
    return x
# end of f(). 

print(f(2))

# EXAMPLE 3

x = 10
y = 5

def f(x, y):
    return x + y
# end of f()

print(f(2,3))
















# EXAMPLE 3

# DO NOT HAVE GLOBAL VARIABLES AFFECT THE VARIABLES INSIDE THE FUNCTION. 

x = 10
y = 5
z = 120

def f(x, y):
    return x + y + z # THIS IS VERY BAD.
# end of f(x)

print(f(2,2))















# EXAMPLE 4
def fib(n):
    memory = {0 : 0, 1 : 1}

    def helper(n):
        if n in memory:
            return memory[n]
        else:
            return helper(n-1) + helper(n-2)

    return helper(x)
# end of fib

print(f"The {10}th fibonnaci number is: {fib(10)}")


''' TRACE TABLE
n           fib(n)
1           1
...         ...
x           fib(x-1)+fib(x+2)
'''












#Example 4

def fib2(n):
    if n== 0:
        return 0
    elif n == 1:
        return 1
    else