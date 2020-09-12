'''Problem Statement :Find minimum possible number after k swaps
Referring Sites : https://www.techiedelight.com/find-minimum-number-possible-k-swaps/
Logic : Used Backtracking
Consider every digit and swap it with digit followed it one at a time and see if it leads to a minimum number,The whole process is repeated
K times'''
# A utility function to swap the ith and jth element of a list c
# ch acts as a temporary variable

def swap(c, i, j):
    ch = c[i]
	c[i] = c[j]
	c[j] = ch

# Main function
def findMinimum(digits, n, k, min_so_far):
    # compare current number with minimum number so far
	num = int("".join(digits))

    # Case where current number is less than minimum so far 
	if num < min_so_far:
		min_so_far = num
    
    # Base case where no more swap operations are allowed
	if k < 1:
		return min_so_far
    
    # do for each digit in input
	for i in range(n - 1):
        for j in range(i + 1, n):

            # Case where the digit at ith index is greater than jth index
            # in that case they will be swapped
            if digits[i] > digits[j]:
				swap(digits, i, j)
                min_so_far = findMinimum(digits, n, k - 1, min_so_far)
                swap(digits, i, j)

	return min_so_far

# Driver code
if __name__ == '__main__':
    
	i = 934651
	k = 2
    # convert digits of the given integer into a list of strings to
	# facilitate operations on them
	digits = list(str(i))
	minimum = findMinimum(digits, len(digits), k, i)
    print("The minimum number formed by doing at-most {k} swaps is {minimum}")
