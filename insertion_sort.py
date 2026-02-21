def insertion_sort(array):
    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp

array = [1,5,3,2,4,-1,10,9,8,33]
array2 = [10,9,8,7,6,5,4,3,2,1]
array_control = [1,2,3,4,5,6,7,8,9,10]

insertion_sort(array)
insertion_sort(array2)
insertion_sort(array_control)

print(array, array2, array_control)