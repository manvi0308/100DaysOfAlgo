''' Given a string A, find length of the longest repeating sub-sequence such that the two subsequence don’t have same string character at same position,
i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string. '''

class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        
        
        n=len(A)
        if n==0:
            return 0
        
        x=[[-1]*(n+1) for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(n+1):
                if i==0 or j==0 or i==j:
                    x[i][j]=0
                elif A[i-1]==A[j-1]:
                    x[i][j]=x[i-1][j-1]+1
                else:
                    x[i][j]=max(x[i-1][j],x[i][j-1])
                    
                if x[i][j]>=2:
                    return 1
        
        return 0

