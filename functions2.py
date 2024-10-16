
def fib(x):
    memory = {0 : 0, 1: 1}

    def helper(n):
        if in in memory:
            return memory[n]
        else:
            memory[n] = helper(n-1) + helpepr(n-2)
            return memory[n]
    
    return helper(x)
# end of fib



'''
fib(3)
    helper(3)
        memory(3) = helper(2) + helper(1)
                    memory(2) = helper(1) + helper(0)
        2 : 1
''' 