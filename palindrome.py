# A word that is the same forwards and backwards 
# e.g. tacocat, skibiks are palindromes
# tacodogs, skibidi isn't.

def isPalindrome(word : str) -> bool: #type hinting
    # def isPalindrome(word): is perfectly acceptabe
    # Base cases are the simplest cases, and a systematic and holistic approach to coding
    # Base case -> Empty strings are inded palindromes. Base cases are the simplist cases
    if not word: #if len(word) == 0: is also valid
        return True
    # Base case #2 -> a single character is a palindrome
    elif len(word) == 1:
        return True
    # Base Case #3 -> strings with 2 or 3 characters. This can only be applied if the previous two checks proved false.
    elif len(word) <= 3: #Less comparison and operations in general make the program more efficient. This is how we optimize programming.
        return True
    # Lets dissect it for real now.
    # H  E  L  L  O
    # 0  1  2  3  4
    # -5 -4 -3 -2 -1
    # Lets imagine it like this. We need to check if 0 and 4, or -5 and -1 are equal.
    else:
        # what do we do if our length is >3...? 
        # DON'T CONVERT TO SET REMEMBER SETS DON'T HAVE DUPLICATES
        # Don't need to convert to a list.
        # There are multiple solutions always. 

        # Solution 1: split down the middle then compare
        # Solution 2: Reverse the word into a separate variable and then compare equality
        # Solution 3: Traverse forwards and backwards for equality
        # Now... which one is the most efficient?
        # DECOMPOSITION: Lets do 2
        # We need to make a separate variable.
        flipped = word[::-1] # OR flipped = ''.join(reversed(word)). This is VERY VERY VERY IMPORTANT. I should memorize [::-1] for any sliceable thingy, I can REVERSE IT. REVERSING IS PYTHON'S SPECIALTY.
        # Sometimes we should check if it ISN'T a palindrome. NOT RIGHT NOW THOUGH
        return flipped == word

word = input()
print(isPalindrome(word))



'''
ChatGPT:
def is_palindrome(word):
    # Convert the word to lowercase to make the check case-insensitive
    word = word.lower()
    # Reverse the word and store it in a separate variable
    reversed_word = word[::-1]
    # Check if the original word is equal to the reversed word
    return word == reversed_word

# Example usage
word = "Racecar"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

'''