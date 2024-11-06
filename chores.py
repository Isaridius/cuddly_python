# 1. MAKE TASKS
t = int(input())
c = int(input())
task = []

for i in range(c):
    task.append(int(input()))


# 2. SORT TASK
def mergeSort(array):
    if len(array) <= 1:
        return array
    # end of base case

    left = [] # Division of array : left half
    right = [] # Divsion of array : right half

    for i in range(len(array)):
        if i < (len(array) // 2):
            left.append(array[i])
        else:
            right.append(array[i])
    # end of division

    # recursive mergeSort of left and right
    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)
# end of mergeSort()

print(mergeSort(task))
