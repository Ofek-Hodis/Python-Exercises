example_array = [1,2,5,9,12,17,26,43,45,46,47,48,51,52,67,70,71,72,87,98,99,100]

def binary_search(array, target): # A classic binary search function, complexity O(logn)
    low = 0
    high = len(array) - 1
    while low<=high:
        mid = (low+high)//2
        value = array[mid]

        if value == target: return mid
        elif value < target: low = mid + 1
        elif value > target: high = mid - 1
    return -1 # If the value was not found, -1 will be returned to indicate it does not exist

def binary_search_recursive(array, target, low, high):
    if low > high:
        return -1
    mid = (low+high)//2
    value = array[mid]
    if value == target: return mid
    elif value < target:
        return binary_search_recursive(array, target, mid + 1, high)
    elif value > target:
        return binary_search_recursive(array, target, low, mid-1)

target = int(input("Enter a target number: "))
print(binary_search(example_array, target))
print(binary_search_recursive(example_array, target, 0, len(example_array)-1))
