''' Problem statement : Given an array of integers, find the length of the longest sub-sequence such that elements in the
subsequence are consecutive integers, the consecutive numbers can be in any order


Algorithm: 

Create an empty hash.
Insert all array elements to hash.
Do following for every element arr[i]
Check if this element is the starting point of a subsequence. To check this, simply look for arr[i] – 1 in the hash, if not found, then this is the first element a subsequence.
If this element is the first element, then count the number of elements in the consecutive starting with this element. Iterate from arr[i] + 1 till the last element that can be found.
If the count is more than the previous longest subsequence found, then update this.

Time complexity : O(n)
Space complexity : O(n)
'''

# Python program to find longest contiguous subsequence

from sets import Set


def findLongestConseqSubseq(arr, n):

	s = Set()
	ans = 0

	# Hash all the array elements
	for ele in arr:
		s.add(ele)

	# check each possible sequence from the start
	# then update optimal length
	for i in range(n):

		# if current element is the starting
		# element of a sequence
		if (arr[i]-1) not in s:

			# Then check for next elements in the
			# sequence
			j = arr[i]
			while(j in s):
				j += 1

			# update optimal length if this length
			# is more
			ans = max(ans, j-arr[i])
	return ans

