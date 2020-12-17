''' Problem statement : The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3 ) :

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"
Given n and k, return the kth permutation sequence. 

Approach : This involves a little bit of maths and recursion for simplicity.

Number of permutation possible using n distinct numbers = n!

Lets first make k 0 based.
Let us first look at what our first number should be.
Number of sequences possible with 1 in first position : (n-1)!
Number of sequences possible with 2 in first position : (n-1)!
Number of sequences possible with 3 in first position : (n-1)!

Hence, the number at our first position should be k / (n-1)! + 1 th integer.'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, n, k):
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])
        return permutation
