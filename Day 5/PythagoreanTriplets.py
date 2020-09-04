# Find a pythagorean triplet in the given array
# Problem Statement: Given an array of integers write a functon that returns true if there is a triplet (a, b, c) that satisfies a^2 = b^2+c^2

import math
def checkTriplet( arr, n):
    maximum = 0
    for i in range(n):
        maximum = max(maximum , arr[i]) # For finding maximum element
    
    hash = [0] * (maximum + 1) #Hashing array
    for i in range(n):
        hash[arr[i]] += 1 #Increasing the count of array elements in hash table 
    
    for i in range(1 , maximum+1):
        if(hash[i] == 0): #In case , a is not there
            continue
        for j in range(1, maximum+1): #Iterating for all possible b
            if((i==j and hash[i] == 1) or hash[j] == 0):
                continue
            val = int(math.sqrt(i*i +j*j))
            if((val * val) != (i*i +j*j)): #Case where c^2 is not a perfect square
                continue
            if(val > maximum): # Case where c exceeds maximum value
                continue
            if (hash[val]):# However if c exists in original array , then we have the triplet
                return True
    return False
arr = [1,2,3,4,5]
n = len(arr)
if (checkTriplet(arr , n)):
    print('Pythagorean Triplet Found')
else:
    print('Pythagorean Triplet do not Found')