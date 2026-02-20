def bubble_sort(array):
    for i in range(len(array)):
        j = i
        while j > 0:
            if array[j] < array[j-1]:
                placeholder = array[j]
                array[j] = array[j-1]
                array[j-1] = placeholder
            j -= 1

def bubble_sort_2(array):
    is_changed = True
    while is_changed:
        is_changed = False
        j=0
        while j in range(len(array)-1):
            if array[j] > array[j+1]:
                placeholder = array[j]
                array[j] = array[j+1]
                array[j+1] = placeholder
                is_changed = True
            j+=1

array = [1,5,3,2,4,-1,10,9,8]
array2 = [10,9,8,7,6,5,4,3,2,1]
bubble_sort_2(array)
bubble_sort_2(array2)
print(array, array2)