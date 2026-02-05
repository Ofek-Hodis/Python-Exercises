def interpolation_search(array, target):
    low = 0
    high = len(array) - 1

    while (target >= array[low]) and (target <= array[high]) and low<=high:
        # Interpolation search formula taking into consideration data set's length and estimated location of target
        probe = int(low + (high-low) * (target-array[low])/(array[high]-array[low])) #Cast to int to represent an index
        if array[probe] == target: return probe
        elif array[probe] < target: low = probe+1
        else: high = probe-1

    return -1 # If the value is not found the method returns -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 16, 19, 21, 22, 33, 34, 56]
target = int(input("Enter a target number: "))
result = interpolation_search(array, target)

print ("The index of your target is: " + str(result))