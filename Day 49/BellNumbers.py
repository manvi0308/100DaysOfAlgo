''' Given a set of n elements, find number of ways of partitioning it.

What is Bell Number?
Let S(n, k) be total number of partitions of n elements into k sets. The value of n’th Bell Number is sum of S(n, k) for k = 1 to n.
Bell(n) =  \sum_{k=0}^{n}S(n,k) 
Value of S(n, k) can be defined recursively as, S(n+1, k) = k*S(n, k) + S(n, k-1)'''

# A Python program to find n'th Bell number 

def bellNumber(n): 

	bell = [[0 for i in range(n+1)] for j in range(n+1)] 
	bell[0][0] = 1
	for i in range(1, n+1): 

		# Explicitly fill for j = 0 
		bell[i][0] = bell[i-1][i-1] 

		# Fill for remaining values of j 
		for j in range(1, i+1): 
			bell[i][j] = bell[i-1][j-1] + bell[i][j-1] 

	return bell[n][0] 

# Driver program 
for n in range(6): 
	print('Bell Number', n, 'is', bellNumber(n)) 
