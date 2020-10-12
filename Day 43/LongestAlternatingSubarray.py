# Function to find length of longest sublist with alternating
# positive and negative elements
def findLongestSubList(A):

	# stores length of longest alternating sublist found so far
	maxLen = 1

	# stores ending index of longest alternating sublist found so far
	endIndex = 0

	# stores length of longest alternating sublist ending at current position
	currLen = 1

	# traverse the given list starting from the second index
	for i in range(1, len(A)):

		# if current element has opposite sign than the previous element
		if A[i] * A[i - 1] < 0:

			# include current element in longest alternating sublist ending at
			# previous index
			currLen = currLen + 1

			# update result if current sublist length is found to be greater
			if currLen > maxLen:
				maxLen = currLen
				endIndex = i

		# reset length if current element has same sign as previous element
		else:
			currLen = 1

	sublist = A[endIndex - maxLen + 1: endIndex + 1]
	print("The longest alternating sublist is:", sublist)


if __name__ == '__main__':

	A = [1, -2, 6, 4, -3, 2, -4, -3]
	findLongestSubList(A)
