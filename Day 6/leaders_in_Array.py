# Leaders in an Array
''' Problem Statement: Write a program to print all leaders in array.An element is leader if its greater than all the elements
to its right side.And the rightmost element is always a leader
Time complexity is O(n)
Space Complexity is O(1)'''
#Note the naive approach of taking two loops and scanning every element then comparing it with every element to the right will take O(n^2) time complexity

# Function for finding the leaders
def leadersArray(arr, size):
    max = arr[size-1] # The rightmost element will always be a leader
    print(max)
    for i in range(size-2 ,-1 , -1): #Start a loop from the second rightmost position , keep on moving till leftmost position
        if max <= arr[i]:
            print(arr[i]) #In that case  it will be a leader
            max = arr[i] #Now max value will become arr[i]

# Driver code
array = [16,17,4,3,5,2]
size_of_array = len(array)
leadersArray(array, size_of_array)
