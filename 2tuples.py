'''
tuples!
Tuples are immutable, allows different datatypes, iterable, and nestable.
    Tupes are ()



(50,) is a singleton tuple, comma required for one thing
tuples are sliceable, and indexable using square brackers

tup = ('C', ' Java', 'Python')
empty_tup = ()
single_tup = ('Park',)






# Concatenation: Joining two tuples
a = (1,2,3)
b = (4,5,6)
concat_result = a + b
print('a+b:', concat_result)
### a+b: (1, 2, 3, 4, 5, 6)

# Repetition: Repeating a list multiple times
c = ('Hi!',)
repet_result = c * 3
print('c*3', repet_result)
### c*3 ('Hi!', 'Hi!', 'Hi!')

# Membership: Check if a value exists in a tuple
d = a + b + c
print('d:', d)
print('\'Hi!\' in d:', 'Hi!' in d)
print('7 in d:', 7 in d)
### d: (1, 2, 3, 4, 5, 6, 'Hi!')
### 'Hi!' in d: True
### 7 in d: False






'''
'''
# Iteration
example = ('C', 'Java', 'Python', 'C#', 'JavaScript')

print('Tuple example items:')
for language in example:
    print(language)
print('--')

# Indexing
print('Index 1:', example[1]) ### prints Java
print('Last Value:', example[-1]) ### Prints Javascript

# Slicing
print('Backwards:', example[::-1]) ### Java - Beginning
print('Every other:', example[::2]) ### Every other
print('From 1 to end:', example[1:]) ### Java - End
print('From 1 to 3:', example[1:3])





# Tuple of Even values from 1 to 100
even_tup = tuple(i for i in range(1,101) if i % 2 == 0)

print(even_tup)



















