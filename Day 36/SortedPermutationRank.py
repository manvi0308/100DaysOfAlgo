''' Problem Statement: Given a string, find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.
Link: https://www.interviewbit.com/problems/sorted-permutation-rank/

Approach: Lets start by looking at the first character.

If the first character is X, all permutations which had the first character less than X would come before this permutation when sorted lexicographically.

Number of permutation with a character C as the first character = number of permutation possible with remaining N-1 character = (N-1)!

Then the problem reduces to finding the rank of the permutation after removing the first character from the set.'''

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        n = len(A)
        a = 0
        B = [a for a in A ]
        B.sort()
        ans = 0
        while(a<len(A)) :
            
            for i in range(len(B)) :
                if B[i] == A[a] :
                    ans += math.factorial(n-1-a)*i
                    B.remove(A[a])
                    B.sort()
                    break
                    
            a+=1
        return (ans+1)% 1000003
