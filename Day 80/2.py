# Python 3 program to make GCD 
# of array a mutiple of k. 
def MinOperation(a, n, k): 
	
	result = 0
	
	for i in range(n) : 
	
		''' If array value is not 1 and it 
		is greater than k then we can 
		increase the or decrease the 
		remainder obtained by dividing 
		k from the ith value of array so 
		that we get the number which is 
		either closer to k or its multiple '''
		if (a[i] != 1 and a[i] > k) : 
			result = (result + min(a[i] % k, 
							k - a[i] % k)) 
		
		else : 

			# Else we only have one choice 
			# which is to increment the value 
			# to make equal to k 
			result = result + k - a[i] 

	return result 

