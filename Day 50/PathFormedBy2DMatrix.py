class Solution:
# @param A : list of list of integers

# @return an integer
    def minPathSum(self, A):
        # base case 
        if(A == [[0]]):
            return 0
        # storing the length of 2D Matrix
        m = len(A)
        
        n = len(A[0])
        
        minSum = [[0]*n]*m
        for i in range(0,m):
            i2 = m-i-1
            for j in range(0,n):
                j2 = n-j-1
                if(i2 == m-1 and j2 == n-1):
                    minSum[i2][j2] = A[i2][j2]
                elif(i2 == m-1 and j2 < n-1):
                    minSum[i2][j2] = minSum[i2][j2+1] + A[i2][j2]
                elif(i2 < m-1 and j2 == n-1):
                    minSum[i2][j2] = minSum[i2+1][j2] + A[i2][j2]
                else:
                    minSum[i2][j2] = min(minSum[i2][j2+1],minSum[i2+1][j2]) + A[i2][j2]
        
        return minSum[0][0]
                    
        
