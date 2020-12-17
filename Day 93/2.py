''' Problem statement : Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["a","a","b"]
    ["aa","b"],
  ]
  
  Approach : When on index i, you incrementally check all substring starting from i for being palindromic. 
  If found, you recursively solve the problem for the remaining string and add it to your solution. Start this recursion from starting position of the string'''
  
  class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        n=len(A)
        res=[]

        def dfs(op,k):
            if k==n:
                res.append(op)
                return
            for i in range(k,n):
                temp=A[k:i+1]
                if temp==temp[::-1]:
                    dfs(op+[temp],i+1)
            
        dfs([],0)
        return res
        
        
        
        
        
        
        
