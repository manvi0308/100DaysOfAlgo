''' Problem Statement : Given an array where every element occurs three times, except one element which occurs only once. Find the element that occurs once. 
Expected time complexity is O(n) and O(1) extra space.


'''


INT_SIZE = 32

def getSingle(arr, n) : 
	
	# Initialize result 
	result = 0
	
	# Iterate through every bit 
	for i in range(0, INT_SIZE) : 
		
		# Find sum of set bits ith position in allarray elements 
		sm = 0
		x = (1 << i) 
		for j in range(0, n) : 
			if (arr[j] & x) : 
				sm = sm + 1
				
		# The bits with sum not multiple of 3, are the  bits of element with single occurrence. 
		if ((sm % 3)!= 0) : 
			result = result | x 
	
	return result 
	
