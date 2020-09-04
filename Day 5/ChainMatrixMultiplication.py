'''Matrix Chain Multiplication using dynamic Programming - Determine the optimal parenthesization of product of n matrices
 Problem  : Given a series of n arrays to multiply A1*A2*A3*......*An.Determine where to place parenthesis to minimize the number of multiplications
 Key Fact : Multipliying an i*j matrix by j*k matrix requires i*j*k operations'''
import sys
def matrixChainOrderMuliplication(p, i, j): #i is starting index of array/list and j is the ending index
    # Base case when only one matrix is there 
    if i==j:
        return 0
    
    _min = sys.maxsize #An integer giving the maximum size a variable of type Py_ssize_t can take
    for k in range(i , j):
        # Recursively place parenthesis at different position between first and last position and calculate count of multiplications for each placement
        count = (matrixChainOrderMuliplication(p, i, k) + matrixChainOrderMuliplication(p, k+1, j) + 
        p[i-1] * p[k] * p[j])

        if count <_min:
            _min = count
    
    return _min
# Function for printing the result
def printResult(val):
    print('Minimum number of multiplications required are : ' + str(val))
# Sample inputs and driver code
array = [40, 20, 30, 10, 30]
n = len(array)
res = matrixChainOrderMuliplication(array, 1, n-1)
printResult(res)
array2 = [1,4,5,6,7,8,9]
n2 = len(array2)
res2 = matrixChainOrderMuliplication(array2, 1, n2-1)
printResult(res2)



