''' Problem Description :- Given an integer A, return the number of trailing zeroes in A!.
Note: Your solution should be in logarithmic time complexity.

**Problem Constraints**
1 <= A <= 10000
'''



class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        # there are no zeroes in numbers less than 5
        
        if A < 5:
            return 0
        
        
        count_of_zeroes = 0
        multiplicant = 5
        while A/multiplicant > 0:
            count_of_zeroes = count_of_zeroes + A/multiplicant
            multiplicant *= 5
        
        return count_of_zeroes
