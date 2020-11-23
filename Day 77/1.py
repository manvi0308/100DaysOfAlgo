''' Problem statement : Given an array, count pairs in the array such that one element of pair divides other.
'''

# Python3 program to count  
# divisible pairs.  
  
def countDivisibles(arr, n) : 
  
    res = 0
  
    # Iterate through all pairs  
    for i in range(0, n) : 
        for j in range(i+1, n) : 
              
            # Increment count if one divides  
            # other  
            if (arr[i] % arr[j] == 0 or
            arr[j] % arr[i] == 0) : 
                res+=1
  
    return res  
