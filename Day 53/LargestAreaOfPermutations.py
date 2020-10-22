''' Problem Description

Given a binary grid A of size N x M consisting of 0's and 1's, find the area of the largest rectangle inside the grid such that all the cells inside the chosen 
rectangle should have 1 in them.
You are allowed to permutate the columns matrix i.e. you can arrange each of the column in any order in the final grid.

I/O Format :
Input Format
First and only argument is an 2D binary array A.
Output Format
Return a single integer denoting the area of the largest rectangle inside the grid such that all the cells inside the chosen rectangle should have 1 in them '''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        r = len(A)
        c = len(A[0])
        maxArea = 0
        for i in range(1,r):
            for j in range(c):
                if A[i][j]:
                    A[i][j] += A[i-1][j]
        for i in range(r):
            A[i].sort(reverse=True)
            for j in range(c):
                maxArea = max(maxArea, (j+1)*A[i][j])
        return maxArea
