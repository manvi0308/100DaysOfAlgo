#  Problem Statement:  Program to print all combination of size r in an array of size n 
def printAllCombinationfSizeR(arr, n, r): 
	data = [0] * r  # A temporary array to store all combination one by one 
    # Print all combination using temprary array 'data[]' 
	combinationUtility(arr, data, 0, n - 1, 0, r)
''' arr[] ---> Input Array 
    data[] ---> Temporary array to store current combination 
    start & end ---> Staring and Ending indexes in arr[] 
    index ---> Current index in data[] 
    r ---> Size of a combination to be printed '''
def combinationUtility(arr, data, start, end, index, r): 
	
    #  Since current combination is ready to be printed so just print it				
	if (index == r): # Since current combination is ready to be printed so just print it
		for j in range(r): 
			print(data[j], end = " ")
		print()
		return
# replace index with all possible elements.The condition "end-i+1 >= r-index" makes sure that including one element at index will make a combination 
# with remaining elements at remaining positions 
	i = start; 
	while(i <= end and end - i + 1 >= r - index): 
		data[index] = arr[i]
		combinationUtility(arr, data, i + 1, 
						end, index + 1, r)
		i += 1
# Driver Code 
arr = [1, 2, 3, 4, 5]
r = 3
n = len(arr)
printCombination(arr, n, r)


