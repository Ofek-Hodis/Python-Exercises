def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j

        temp = array[i]
        array[i] = array[min]
        array[min] = temp

array = [1,5,3,2,4,-1,10,9,8,33]
array2 = [10,9,8,7,6,5,4,3,2,1]
array_control = [1,2,3,4,5,6,7,8,9,10]

selection_sort(array)
selection_sort(array2)
selection_sort(array_control)

print(array, array2, array_control)

