''' Problem Statement: A items are to be delivered in a circle of size B.
Find the position where the Ath item will be delivered if we start from a given position C.
NOTE: Items are distributed at adjacent positions starting from C

Approach: We check if the number of items to be distributed is greater than our remaining positions in current cycle of circle or not.
If yes, then we simply return A + C – 1 (We distribute items in same cycle starting from C). Else we compute number of remaining items after completing current cycle 
and return mod of remaining items. '''

# n ==> Size of circle 
# m ==> Number of items 
# k ==> Initial position 
def lastPosition(n, m, k): 
      
    # n - k + 1 is number of positions 
    # before we reach beginning of circle 
    # If m is less than this value, then 
    # we can simply return (m-1)th position 
    if (m <= n - k + 1): 
       return m + k - 1
   
    # Let us compute remaining items before 
    # we reach beginning. 
    m = m - (n - k + 1) 
   
    # We compute m % n to skip all complete 
    # rounds. If we reach end, we return n 
    # else we return m % n 
    if(m % n == 0): 
        return n 
    else: 
        return m % n 
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        return lastPosition(B,A,C)

