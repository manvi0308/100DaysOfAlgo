''' Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times. '''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        # Create empty resultArr and check if
        # A in None or empty and return empty
        # list i.e. resultArr.
        resultArr = []
        if A==None or len(A)<1:
            return resultArr
        
        # Sort the input list and call recursive
        # function to get all combinations.
        A = sorted(A)
        combination = []
        self.recursiveCombinationSum(resultArr, A, combination, B)
        
        # Sort the received input and remove 
        # redundant entries from resultArr.
        for i in range(len(resultArr)):
            resultArr[i] = sorted(resultArr[i])
        resultArr = sorted(resultArr)
        
        check = 0
        while check<len(resultArr)-1:
            if resultArr[check]==resultArr[check+1]:
                resultArr.pop(check+1)
            else:
                check += 1
        
        return resultArr
    
    def recursiveCombinationSum(self, resultArr, A, combination, B):
        # Add to resultArr if target value is 0.
        if B==0:
            temp = []
            for i in range(len(combination)):
                temp.append(combination[i])
            resultArr.append(temp)
            return
        
        # Recursively call the function to get
        # all the combinations for required sum.
        for i in range(len(A)):
            if A[i]>B:
                break
            combination.append(A[i])
            self.recursiveCombinationSum(resultArr, A, combination, B-A[i])
            combination.pop()

