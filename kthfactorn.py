def factor(n, k):
    # Initialize an empty list for factors
    factors = []
    
    # Loop through numbers from 1 to n-1
    for d in range(1, (n**0.5)-1):  # range should start from 1, and end at n, not n-1
        if n % d == 0:     # use '==' for comparison, not '='
            factors.append(d)

    if len(factors) <= k-1:
        return -1
    else:
        return result[k-1]


def optimize(n,k):
    stop = int(n**0.5)+1
    result = [1,n]
    for divider in range(2, stop):
        if n % divider == 0:
            result.append(divider)
            quotient = n// divider
            if quotient != divider:
                result.append(quotient)
    result.sort()
    if (k-1) >= len(result):
        return -1
    else:
        return result[k-1]
