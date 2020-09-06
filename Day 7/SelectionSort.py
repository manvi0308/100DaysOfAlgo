# Selection sort
import sys
array_to_be_sorted = [64, 25, 12, 22, 11, 67, 99, 1, 34]

# Traversing through all array elements
for i in range(len(array_to_be_sorted)):
    
    # Find the minimum element in remaining unsorted array
    min_index = i
    
    for j in range(i+1 ,len(array_to_be_sorted)):
        
        if array_to_be_sorted[min_index] > array_to_be_sorted[j]:
            min_index = j
    
    # Swapping the found minimum element with the first element
    array_to_be_sorted[i] , array_to_be_sorted[min_index] = array_to_be_sorted[min_index] , array_to_be_sorted[i]

print('Sorted order will be :')
for i in range(len(array_to_be_sorted)):
    print('%d' %array_to_be_sorted[i])