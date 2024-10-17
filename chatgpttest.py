def calculate_average(numbers):
    # Handle the empty list case
    if not numbers:
        return None
    
    # Initialize sum and count
    total_sum = 0
    count = 0
    
    # Loop through the list and add only numeric values
    for num in numbers:
        if isinstance(num, (int, float)):
            total_sum += num
            count += 1
    
    # If no numeric values were found, return None
    if count == 0:
        return None
    
    # Calculate and return the average
    average = total_sum / count
    return average

skibidi = input()
print(calculate_average(skibidi))