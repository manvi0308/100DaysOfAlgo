''' Problem Statement : Given three numbers a, b and k, find k-th digit in ab from right side

Examples: Input : a = 3, b = 3, 
        k = 1
Output : 7
Explanation
3^3 = 27 for k = 1. First digit is 7 in 27

Input : a = 5, b = 2, 
        k = 2
Output : 2
Explanation
5^2 = 25 for k = 2. First digit is 2 in 25'''


def kthdigit(a, b, k): 
	
	# computin a^b in python 
	p = a ** b 
	count = 0
	
	while (p > 0 and count < k): 
		
		# getting last digit 
		rem = p % 10

		# increasing count by 1 
		count = count + 1

		# if current number is required digit 
		if (count == k): 
			return rem 

		# remove last digit 
		p = p / 10; 
	
