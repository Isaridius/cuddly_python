def factor(n, k):
    # Initialize an empty list for factors
    factors = []
    
    # Loop through numbers from 1 to n-1
    for d in range(1, n+1):  # range should start from 1, and end at n, not n-1
        if n % d == 0:     # use '==' for comparison, not '='
            factors.append(d)

    if len(factors) <= k-1:
        return -1
    else:
        return result[k-1]



