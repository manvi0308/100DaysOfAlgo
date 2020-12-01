''' The value of determinant of a matrix can be calculated by following procedure – 
For each element of first row or first column get cofactor of those elements and then multiply the element with the determinant of the corresponding cofactor, 
and finally add them with alternate signs. As a base case the value of determinant of a 1*1 matrix is the single value itself'''. 

Cofactor of an element, is a matrix which we can get by removing row and column of that element from that matrix.


# defining a function to get the minor matrix after excluding i-th row and j-th column.

def getcofactor(m, i, j):
	return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

# defining the function to calculate determinant valueof given matrix a.

def determinantOfMatrix(mat):

	# if given matrix is of order 2*2 then simply return de value by cross multiplyin elements of matrix.
	if(len(mat) == 2):
		value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
		return value

	# initialize Sum to zero
	Sum = 0

	# loop to traverse each column
	# of matrix a.
	for current_column in range(len(mat)):

		# calculating the sign corresponding
		# to co-factor of that sub matrix.
		sign = (-1) ** (current_column)

		# calling the function recursily to
		# get determinant value of
		# sub matrix obtained.
		sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))

		# adding the calculated determinant
		# value of particular column
		# matrix to total Sum.
		Sum += (sign * mat[0][current_column] * sub_det)

	# returning the final Sum
	return Sum



