from math import ceil

#input
print("Indicate how many planks there are by letters in input.")
section1 = input("Enter section 1: ")
section2 = input("Enter section 2: ")
section3 = input("Enter section 3: ")

#processing
cans = len(section1) + len(section2) + len(section3)

boxes = ceil(cans/12)
leftover = 12*boxes - cans

totalcost = 14.95*boxes

#output
print(f"Total cans needed are {cans}. Total boxes of paint are {boxes}. Leftover cans are {leftover}. Total cost is {totalcost})")