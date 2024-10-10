'''strings.
S K I B I D I
0 1 2 3 4 5 6

but also...

S  K  I  B  I  D  I   S  K  I  B  I  D  I
-7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6

you can compare strings, but you can't change them. 
Strings are boolean, and immutable
ord() and chr() find the ASCII of that char, vice versa.

Slicing generates a new string; therefore, slices can be set to a variable
The slice will start and include the value at starting_index
The slice will end at ending_index, but not include the value at the ending_index
The ending_index can be a value greater than the largest index possible
If the step_value is not specified, it is set to: 1
If the slicing values are set to an impossible outcome, it will return an empty string: ''

# Example
Looking at: 'Hello!'

  |  H  |  e  |  l  |  l  |  o  |  !  |
  0     1     2     3     4     5     6

  |  H  |  e  |  l  |  l  |  o  |  !   
 -6    -5    -4    -3    -2    -1

word = 'Hello!'

print('word:', word)
print('----------------------')
print('word[0:6]:', word[0:6])
print('word[0:5]:', word[0:5])
print('----------------------')
print('word[1:4]:', word[1:4])
print('word[:3]:', word[:3])
print('word[2:]:', word[2:])
print('word[:]:', word[:])
print('----------------------')
print('word[0:6:2]:', word[0:6:2])
print('word[::2]:', word[::2])
print('word[1:4:3]:', word[1:4:3])
print('word[::-1]:', word[::-1])
print('word[-5:-2]:', word[-5:-2])
print('word[6:0:-1]:', word[-5:-2])
print('word[-1:-6:-1]:', word[-1:-6:-1])
print('----------------------')
print('Some impossible slices and their results:')
print('word[6:0]:', word[6:0], '<< en empty string has been outputted.')
print('word[:20]:', word[:20], '<< There are no characters beyond the index of 6')
print('word[1:4:-1]', word[1:4:-1], '<< en empty string has been outputted.')

word = 'abcdefghijklmnopqrstuvwxyz'
print(word[0:26])
print(word[0::5])
print(word[10:1:-1])
print('sibidi', word[-26:26:1])


for character in word[::-1]:
    print('Current Character:', character)
'''

'''
# String Operation Examples

word1 = 'Hello, '
word2 = 'World!'

print('word1 + word2:', word1 + word2) # Concatenation

word3 = word1[:-2] # Slicing, resulting slice assigned to variable: word3
print('word3*3:', word3*3) # Repetition

print("'H' in word1:",'H' in word1) # Membership
print("'or' not in word2:", 'or' not in word2)




# Using max() and min() on strings

print("min('HelloWorld!'):", min('HelloWorld!'))
print("max('Hello', 'Goodbye!', 'World!'):", max('Hello', 'Goodbye!', 'World!'))




# Using len() on a string

print("len('Hello, World!'):", len('Hello, World!'))
print("len(''):", len('')) # Empty String
print("len(' '):", len(' ')) # Single whitespace
print(type(''))




# Search Related Methods Examples

example = 'hello world!'
result_1 = example.count('e') # is 1
result_2 = example.count('l') # (single lowercase L) is 3
result_3 = example.count('ll') # (double lowercase L) is 1
print('result_1:', result_1)
print('result_2:', result_2)
print('result_3:', result_3)
print('-'*64)

result_4 = example.find('d') # is 10 … found at index 10
result_5 = example.find('z') # is -1 … not found
result_6 = example.find('or') # is 7 … ‘or’ begins at index 7
print('result_4:', result_4)
print('result_5:', result_5)
print('result_6:', result_6)
print('-'*64)

result_7 = example.index('d') # is 10 … found at index 10
print('result_7:', result_7)
result_8 = example.index('or') # is 7 … ‘or’ begins at index 7
print('result_8:', result_8)
result_9 = example.index('z') # is an error
print('result_9:', result_9)
print('-'*64)







basic string methods
string and lsit data types have special methods
we use a . before the name
e.g. print('Hello {}!'.format('World'))

e.g.
word = 'Skibidi'
test1 = word.replace('i', 'o')
word now = Skobodo

# String to a List examples

phrase1 = 'Hello World!'
print(list(phrase1))

phrase2 = 'Mr. Park'
print(sorted(phrase2))
print('-'*64)

# Using .split()
result1 = 'hello world'.split()
print('result1:', result1)

result2 = 'a,b,c,d,e'.split(',')
print('result2:', result2)

result3 = '1$2$3$4$5'.split('$',2)
print('result3:', result3)


















