''' Problem statement : Given two numbers M and N, the task is to check if the M-th and N-th Fibonacci numbers perfectly divide each other or not.

Approach : A naive approach will be to find the N-th and M-th Fibonacci numbers and check if they are perfectly divisible or not.
An efficient approach is to use the Fibonacci property to determine the result. If m perfectly divides n, then Fm also perfectly divides Fn, else it does not.

Exception: When N is 2, it is always possible as Fibo2 is 1, which divides every other Fibonacci number.'''
def check(n, m): 

	# exceptional case for F(2) 
	if (n == 2 or m == 2 or
		n % m == 0) : 
		print( "Yes" ) 
	
	# if none of the above cases, hence not divisible 
	else : 
		print( "No" ) 

# Driver Code 
m = 3
n = 9
check(n, m) 

# This code is contributed 
# by Smitha 
