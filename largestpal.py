# 1. First create a for in for loop thing for all possible combinations
    # How do we do that?
    # we go by 1*1, 1*2, 1*3... 50*49, 50*50... 99*98, 99*99.
# 2. Everytime that one thing is created, we check if it's a palindrome
# 3. If it is, we check if it's the biggest one so far.
# 4. Repeat until we get to 99 * 99.

def isPalindrome(word : str) -> bool:
    flipped = word[::-1]
    return flipped == word

biggest = 0
factors = ""

for left in range(100,1000):
    for right in range(100,1000):
        product = left * right
        if isPalindrome(str(product)) and product > biggest:
            biggest = product
            factors = f"{left} * {right}"
print(biggest)