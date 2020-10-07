''' Problem Description
Given an integer A you need to find the Ath fibonacci number modulo 109 + 7.
The first fibonacci number F1 = 1
The first fibonacci number F2 = 1
The nth fibonacci number Fn = Fn-1 + Fn-2 (n > 2)

Approach: As A is very large we can not use normal recursion or dynamic programming to find the fibonacci number.
We need to find some more efficient trick.

Method 1: ( Using power of the matrix {{1, 1},{1, 0}} )
This O(A) approach which relies on the fact that if we n times multiply the matrix M = {{1, 1},{1, 0}} to itself (in other words calculate power(M, n )), then we get the (n+1)th Fibonacci number as the element at row and column (0, 0) in the resultant matrix.

The matrix representation gives the following closed expression for the Fibonacci numbers:


This method can be optimized to work in O(LogA) time complexity.
We can do recursive multiplication to get power(M, n) in the previous method using this trick.

Time Complexity: O(LogA)
Extra Space: O(LogA) if we consider the function call stack size, otherwise O(1).'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        import numpy as np
    
        by = 10**9+7
        if A in [1,2]:
            return 1
        import numpy as np
        M = np.matrix([[1,1],[1,0]],dtype=int)
        
        def ret(N):
            if N == 1 :
                return M
            M1 = ret(N//2)
            if N%2:
                return (M1*M1*M)%by
            else :
                (M1*M1)%by
        
        return np.array(ret(A-1))[0][0]

