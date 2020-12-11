''' Problem statement : Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]  

Approach : Lets say we are at index start then we can swap element at this index with any index>start and permute the elements starting from start+1 using recursion. 
You can swap back the elements at start and index in order to maintain the order for next recursive call 

'''

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if(len(A) == 1):
            return [A]
        res = []
        for i in range(len(A)):
            nxt = self.permute(A[:i] + A[i+1:])
            for j in nxt:
                res.append([A[i]] + j)
        return res
