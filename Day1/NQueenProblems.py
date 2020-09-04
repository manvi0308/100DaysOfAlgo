#  The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack
#  each other.

'''Sources: https://www.programiz.com/python-programming/methods/built-in/zip (For built in method zip())
Classic explanation of Backtracking: https://www.codesdope.com/blog/article/backtracking-explanation-and-n-queens-problem/
A utility function to check if a queen can be placed on board[row][col]. Note that this function is called when "col" queens are 
already placed in columns from 0 to col -1.So we need to check only left side for attacking queens '''

def isSafe(board, row, col):
    # Checking on upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: #In that case it is already occupied
            return False
    
    # Checking lower diagonal
    for i,j in zip(range(row,N,1),range(col , -1 , -1)):
        if board[i][j] == 1:
            return False

    # Checking row on left side 
    for i in range(col): 
        if board[row][i] == 1: 
            return False
    
    return True  #  After passing all the above three constraints

# A recursive function that recurs over the columns to get an optimal solution
def Nqueenssproblem(board, col): 
      
    # Taking base case if all queens will be placed then return True
    if col >= N: 
        return True
  
    
    for i in range(N): 
  
        if isSafe(board, i, col): #Checking for that prerequisite function
              
            # Place this queen in board[i][col] 
            board[i][col] = 1
  
            # recur now for rest of the queens
            if Nqueenssproblem(board, col + 1) == True: 
                return True
            else:
            board[i][col] = 0 # Remove queen from that position if it don't gives a feasible solution
  
    # if the queen can not be placed in any row in this colum col then return false 
    return False

# Main function
def placeQueens(): 
    board = [ [0, 0, 0, 0, 0], # A sample problem for 5 queens
              [0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]] 
  
    if Nqueenssproblem(board, 0) == False:  # No safe sequence is possible
        print ("Solution does not exist") 
        return False
  
    printSolution(board)  
    return True
  
global N # It will be used several times in the function
N = 5

# A utility function to print the solution
def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 
        print() 
# Driver Code 

print('The solution for N Queens is as : 1 Represent Queens , 0 represent Empty places')
placeQueens() 
  