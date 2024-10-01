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