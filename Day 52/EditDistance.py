''' Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

1) Insert a character
2) Delete a character
3) Replace a character
'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, word1: str, word2: str) -> int:
        dp = list(range(len(word2) + 1))
        
        for i in range(1, len(word1) + 1):
            dp_next = [i] + [0] * len(word2)
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp_next[j] = dp[j - 1]
                else:
                    dp_next[j] = min(dp[j - 1], dp[j], dp_next[j - 1]) + 1
            dp = dp_next
        
        return dp[len(word2)]
