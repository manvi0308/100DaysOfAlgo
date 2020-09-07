def isPositionSafe(matrix, row, column): # Checking for same colums
    for i in range(row):
        if matrix[i][column] == 'Q':
            return False
    (i, j) = (row, column) # Checking for lower diagonal
    while i>=0 and j>=0:
        if matrix[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1
    (i, j) = (row, column)
    while i>=0 and j<N:
        if matrix[i][j] == 'Q':
            return False
        i = i -  1
        j = j +  1  
    return True
def nQueensProblemWithAllSolutions(matrix, row):
    if row == N:
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end = '')
            print()
        print()
        return
    for i in range(N):
        if isPositionSafe(matrix, row, i):
            matrix[row][i] = 'Q'
            nQueensProblemWithAllSolutions(matrix, row+1)
            matrix[row][i] = '-'
if __name__ == '__main__':
    N = 4
    matrix = [['-'for x in range(N)] for y in range(N)]
    nQueensProblemWithAllSolutions(matrix, 0)

        
