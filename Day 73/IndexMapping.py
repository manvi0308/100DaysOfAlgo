''' Problem statement : Given a limited range array contains both positive and non-positive numbers, i.e., 
elements are in the range from -MAX to +MAX. Our task is to search if some number is present in the array or not in O(1) time.

Complexity for searching and inserting is O(1)

Approach : To search any element x in the array.

If X is non-negative check if hash[X][0] is 1 or not. If hash[X][0] is one then the number is present else not present.
If X is negative take absolute value of X and then check if hash[X][1] is 1 or not. If hash[X][1] is one then the number is present'''



# Python3 program to implement direct index  mapping with negative values allowed. 

# Searching if X is Present in the  given array or not. 
def search(X): 

	if X >= 0: 
		return has[X][0] == 1

	# if X is negative take the absolute 
	# value of X. 
	X = abs(X) 
	return has[X][1] == 1

def insert(a, n): 

	for i in range(0, n): 
		if a[i] >= 0: 
			has[a[i]][0] = 1
		else: 
			has[abs(a[i])][1] = 1

