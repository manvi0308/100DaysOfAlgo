''' Problem statement :
Given an array of n integers, find the sum of f(a[i], a[j]) of all pairs (i, j) such that (1 <= i < j <= n).

Approach : se a map/hash function to keep a count of every occurring numbers and then traverse through the list. While traversing through the list,
we multiply the count of numbers that are before it and the number itself. Then subtract this result with the pre-sum of the number before that number
to get the sum of difference of all pairs possible with that number. To remove all pairs whose absolute difference is <=1, simply subtract the count 
of occurrence of (number-1) and (number+1) from the previously computed sum. Here we subtract count of (number-1) from the computed sum as it had
been previously added to the sum, and we add (number+1) count since the negative has been added to the pre-computed sum of all pairs.

Time complexity : O(n)'''



# Function to calculate the sum 
def sum(a, n): 

	# map to keep a count of occurrences 
	cnt = dict() 

	# Traverse in the list from start to end 
	# number of times a[i] can be in a pair and 
	# to get the difference we subtract pre_sum. 
	ans = 0
	pre_sum = 0
	for i in range(n): 
		ans += (i * a[i]) - pre_sum 
		pre_sum += a[i] 

		# if the (a[i]-1) is present then 
		# subtract that value as f(a[i], a[i]-1)=0 
		if (a[i] - 1) in cnt: 
			ans -= cnt[a[i] - 1] 

		# if the (a[i]+1) is present then add that 
		# value as f(a[i], a[i]-1)=0 here we add 
		# as a[i]-(a[i]-1)<0 which would have been 
		# added as negative sum, so we add to remove 
		# this pair from the sum value 
		if (a[i] + 1) in cnt: 
			ans += cnt[a[i] + 1] 

		# keeping a counter for every element 
		if a[i] not in cnt: 
			cnt[a[i]] = 0
		cnt[a[i]] += 1
	
	return ans 

