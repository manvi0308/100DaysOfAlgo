'''Problem Statement : Merge an array of size n into another array of size n
Constraints : In array with size m+n there are n vacant positions and array with size n is having n elements
              Output should be sorted.
Approach    : first move all the elements(hoich are not null) in array of size m+n to the last.For example if the input array is [1, 0, 0, 2, 7, 0].
Then after this operation the array will become [0, 0, 0, 1, 2, 7] i.e. by this we have all the elements which are not null to the end
Next i start from the nth element i.e. in the example quoted above start from 3rd element i.e. 1 and compare it with the 0th element of array
with size n, whichever is smaller will be placed in the 0th index of array of size m + n

Time complexity : O(m+n)'''

def move_m_elements_to_end_of_array(array_mPlusn, size):
    i = 0
    j = size - 1
    for i in range(size - 1, -1 , -1):
        if array_mPlusn[i] != 0:
            array_mPlusn[j] = array_mPlusn[i]
            array_mPlusn[i] = 0
            j -= 1
    
    return array_mPlusn

def merge_arrays(array_mPlusn, array_n, m, n):
    i = n  #iterator variable for nth element in array of size m + n
    j = 0  #iterator variable for 1st element in array of size n
    k = 0 #iterator variable for output array of size m + n
    '''There will be two cases here - 1) If nth element of array of size m + n is smaller than jth element of array of size n, then clearly it
    will be placed in the output array and 2) If the elements in array of size n have been finished in that case also elements from array of size
    m + n will be placed in the output array'''
    while k < (m + n):
        if ((i <(m + n) and array_mPlusn[i] <= array_n[j]) or (j == n)):
            array_mPlusn[k] = array_mPlusn[i]
            k += 1
            i += 1
        
        else:
            array_mPlusn[k] = array_mPlusn[j]
            k += 1
            j += 1

# A simple function to print an array
def printArray(arr , size):
    for i in range(size):
        print(arr[i], ' ', end = '')
    print()

array_mPlusn_demo = [0, 1, 0, 17, 8, 0, 6]  # m + n = 7
array_n_demo      = [4, 5, 13]
mPlusn            = len(array_mPlusn_demo)
n_demo            = len(array_n_demo)
m_demo            = mPlusn - n_demo
move_m_elements_to_end_of_array(array_mPlusn_demo, mPlusn)
merge_arrays(array_mPlusn_demo, array_n_demo,m_demo, n_demo)
printArray(array_mPlusn_demo, mPlusn )











