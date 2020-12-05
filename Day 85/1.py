''' Ways to reach the bottom-right corner of a matrix with exactly k turns allowed'''


# Function to check whether (i, j) is valid matrix coordinate or not
def isValid(i, j):
    return 0 <= i < M and 0 <= j < N
 
 
# Recursive function to count number of different ways to reach the last
# cell (M-1,N-1) of a matrix from the given cell (i,j) with k turns left.
# isCol flag is true when current direction is a column false otherwise
def totalWays(i, j, k, isCol):
 
    # if number of turns are exhausted or if the cell is invalid
    if k == -1 or not isValid(i, j):
        return 0
 
    # if destination is reached with exactly k turns
    if k == 0 and i == M - 1 and j == N - 1:
        return 1
 
    # if the current direction is a column
    if isCol:
        # 1. continue moving a column
        # 2. turn right and decrement number of turns by 1
        return totalWays(i + 1, j, k, isCol) + totalWays(i, j + 1, k - 1, not isCol)
 
    # if the current direction is a row
    # 1. continue moving a row
    # 2. turn down and decrement number of turns by 1
    return totalWays(i, j + 1, k, isCol) + totalWays(i + 1, j, k - 1, not isCol)
 
 
# Function to count number of different ways to reach the bottom-right corner
# of a matrix from its top-left corner with exactly k turns allowed.
def findTotalWays(k, i=0, j=0):
 
    # Recur by moving a column and a row
    return totalWays(i + 1, j, k, True) + totalWays(i, j + 1, k, False)
 
 


