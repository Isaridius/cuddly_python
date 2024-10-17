def mean(a_list_):
    # long way:
    total = 0
    counter = 0 #initalization
    for value in a_list:
        total += value
        counter += 1

    average = total / counter
    return average
    # shorter way, but IB doesn't accept this
    return sum(a_list) / len(a_list)






def median(a_list):
    m = len(a_list) // 2 # let m be midpoint
    sorted_list = sorted(a_list)

    if len(a_list) % 2 == 0:
        # length is even
        left = a_list[m-1]
        right = a_list[m]
        average = (left + right) / 2
        return average
    else:
        # length is odd
        return sorted_list[m]


'''what if we dont know how to sort?

EASIEST SORTING ALGORITHM TIME:
Unsorted list
1. declare empty list called ANSWER
2. while the unsorted list is not empty
3. append min(unsorted list) to ANSWER
4. remove min(unsorted list) from unsorted list