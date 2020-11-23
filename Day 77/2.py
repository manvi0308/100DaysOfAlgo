''' Problem statement : Given two arrays with size n, maximize the first array by using the elements from the second array such that the new array formed contains n 
greatest but unique elements of both the arrays giving the second array priority(All elements of second array appear before first array). The order of appearance of
elements is kept same in output as in input.

Approach : create an auxiliary array of size 2*n and store the elements of 2nd array in auxiliary array, and then we will store elements of 1st
array in it. After that we will sort auxiliary array in decreasing order. To keep the order of elements according to input arrays we will use 
hash table. We will store 1st n largest unique elements of auxiliary array in hash table. Now we traverse the second array and store that elements 
of second array in auxiliary array that are present in hash table. Similarly we will traverse first array and store the elements that are present 
in hash table. In this way we get n unique and largest elements from both the arrays in auxiliary array while keeping the order of appearance of
elements same.
'''

# Function to maximize array elements 
def maximizeArray(arr1, arr2, n): 
      
    # Auxiliary array arr3 to store 
    # elements of arr1 & arr2 
    arr3 = [0] * (2 * n) 
    k = 0
      
    for i in range(n): 
        arr3[k] = arr1[i] 
        k += 1
          
    for i in range(n): 
        arr3[k] = arr2[i] 
        k += 1
  
    # Hash table to store n largest 
    # unique elements 
    hash = {} 
  
    # Sorting arr3 in decreasing order 
    arr3 = sorted(arr3) 
    arr3 = arr3[::-1] 
  
    # Finding n largest unique elements 
    # from arr3 and storing in hash 
    i = 0
    while (len(hash) != n): 
  
        # If arr3 element not present in hash, 
        # then store this element in hash 
        if (arr3[i] not in hash): 
            hash[arr3[i]] = 1
  
        i += 1
  
    # Store that elements of arr2 in arr3 
    # that are present in hash 
    k = 0
    for i in range(n): 
  
        # If arr2 element is present in  
        # hash, store it in arr3 
        if (arr2[i] in hash): 
            arr3[k] = arr2[i] 
            k += 1
              
            del hash[arr2[i]] 
  
    # Store that elements of arr1 in arr3 
    # that are present in hash 
    for i in range(n): 
  
        # If arr1 element is present  
        # in hash, store it in arr3 
        if (arr1[i] in hash): 
            arr3[k] = arr1[i] 
            k += 1
              
            del hash[arr1[i]] 
  
    # Copying 1st n elements of 
    # arr3 to arr1 
    for i in range(n): 
        arr1[i] = arr3[i] 
  
# Function to prarray elements 
def printArray(arr, n): 
      
    for i in arr: 
        print(i, end = " ") 
          
    print() 
