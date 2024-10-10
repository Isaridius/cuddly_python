'''tracetables'''
n = 1216 #Initalizing N
x = 0 #Initalizing X
while n>0: #When N is greater than 0
    x = x + n%10
    n = n/10
print(x)


'''
TRACE TABLES:
n           x
1216        0
121         6
12          7
1           9
0           10
'''