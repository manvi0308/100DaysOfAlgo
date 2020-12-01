# Python3 program to rotate a matrix by 90 degrees 
N = 4

# An Inplace function to rotate 
# N x N matrix by 90 degrees in 
# anti-clockwise direction 
def rotateMatrix(mat): 
	
	# Consider all squares one by one 
	for x in range(0, int(N / 2)): 
		
		# Consider elements in group 
		# of 4 in current square 
		for y in range(x, N-x-1): 
			
			# store current cell in temp variable 
			temp = mat[x][y] 

			# move values from right to top 
			mat[x][y] = mat[y][N-1-x] 

			# move values from bottom to right 
			mat[y][N-1-x] = mat[N-1-x][N-1-y] 

			# move values from left to bottom 
			mat[N-1-x][N-1-y] = mat[N-1-y][x] 

			# assign temp to left 
			mat[N-1-y][x] = temp 


# Function to print the matrix 
def displayMatrix( mat ): 
	
	for i in range(0, N): 
		
		for j in range(0, N): 
			
			print (mat[i][j], end = ' ') 
		print ("") 
	
	
