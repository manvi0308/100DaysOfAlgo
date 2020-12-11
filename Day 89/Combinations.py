''' Problem statement : Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

1) Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
2) Entries should be sorted within themselves. 


Approach : For every element, you have 2 options. You may either include the element in your subset or you will not include the element in your subset.
Make the call for both the cases.
'''




class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        def comb(A,B):
            if B<=0:
                return []
            if B==1:
                return [[a] for a in A]
            ans=[]
            for i in range(len(A)):
                ans+=[[A[i]]+c for c in comb(A[i+1:],B-1)]
            return ans
        
        A=list(range(1,A+1))
        return comb(A,B)
