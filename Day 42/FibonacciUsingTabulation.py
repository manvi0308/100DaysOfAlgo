# Python program Tabulated (bottom up) version 
def fib(n): 

	# array declaration 
	f = [0]*(n+1) 

	# base case assignment 
	f[1] = 1

	# calculating the fibonacci and storing the values 
	for i in range(2 , n+1): 
		f[i] = f[i-1] + f[i-2] 
	return f[n] 

# Driver program to test the above function 
def main(): 
	n = 9
	print("Fibonacci number is " , fib(n))

if __name__=="__main__": 
	main()
