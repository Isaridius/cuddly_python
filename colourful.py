red_votes = 0
blue_votes = 0
votes = input("Votes: ")

lengthvotes = len(votes)
if lengthvotes > 20:
    print("Too many votes")
else:
    for person in votes:
        if person == 'R':
            red_votes += 1
        else:
            blue_votes += 1

    print("Red votes:", red_votes)
    print("Blue votes:", blue_votes)

    red_real_votes = red_votes - 1
    print("Red real votes:", red_real_votes)

    if red_real_votes > blue_votes:
        print("Red wins")
    elif red_real_votes == blue_votes:
        print("Purple; tie")
    else:
        print("Blue wins")