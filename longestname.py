name = '' #initalization
longest_name = ''
longest_length = 0


while name != 'x':
    name = input()
    if name != 'x':
        length = len(name)
        if length > longest_length:
            longest_name = name
            longest_length = length
    else:
        print("End of the inputs.")

if longest_name != '':
    print(f'The longest name with {longest_length} characters is {longest_name}.')
else:
    print('Not enough data.')