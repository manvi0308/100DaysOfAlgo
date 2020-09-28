/* Problem Statement : Sum of pairiwise hammming distances
Suppose the given array contains only binary numbers, i.e A[i] belongs to [0, 1].

Let X be the number of elements equal to 0, and Y be the number of elements equals to 1.

Then, sum of hamming distance of all pair of elements equals 2XY, as every pair containing one element from X and one element from Y contribute 1 to the sum.

As A[i] belongs to [0, 231 - 1] and we are counting number of different bits in each pair, we can consider all the 31 bit positions independent.*/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
    	# an empty array
        array=[]
        total=0
        for i in A:
            array.append('{0:032b}'.format(i))
        array=list(zip(*array))
        for i in array:
            a=i.count("0")
            total+=2*a*(len(i)-a)
        return total%1000000007
