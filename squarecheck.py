print("How many tiles y'all have?")
tiles = int(input())

from math import sqrt, floor

# answer = tiles ** 0.5
# answer = floor(sqrt(tiles))
answer = sqrt(tiles)
answer = floor(answer)

print(f"The largest square had a side length {answer}.")