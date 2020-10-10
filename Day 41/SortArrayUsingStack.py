# Python3 program to sort an array using stack 

# This function return the sorted stack 
def sortStack(input): 
	tmpStack = [] 
	while (len(input) > 0): 
	
		# pop out the first element 
		tmp = input[-1] 
		input.pop() 

		# while temporary stack is not empty 
		# and top of stack is smaller than temp 
		while (len(tmpStack) > 0 and tmpStack[-1] < tmp): 
		
			# pop from temporary stack and 
			# append it to the input stack 
			input.append(tmpStack[-1]) 
			tmpStack.pop() 
		
		# append temp in tempory of stack 
		tmpStack.append(tmp) 
	
	return tmpStack 

def sortArrayUsingStacks(arr, n): 

	# append array elements to stack 
	input = [] 
	i = 0
	while ( i < n ): 
		input.append(arr[i]) 
		i = i + 1
		
	# Sort the temporary stack 
	tmpStack = sortStack(input) 
	i = 0
	
	# Put stack elements in arrp[] 
	while (i < n): 
		arr[i] = tmpStack[-1] 
		tmpStack.pop() 
		i = i + 1
		
	return arr 


