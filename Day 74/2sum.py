''' Problem statement : Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers 
(both index1 and index2 ) are not zero-based.Put both these numbers in order in an array and return the array from your function ( Looking at the function signature
will make things clearer ). Note that, if no pair exists, return empty list.
If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.



Approach : O(n^2) runtime, O(1) space – Brute force:

The brute force approach is simple. Loop through each element x and find if there is another value that equals to target – x. As finding another value requires looping through the rest of array, its runtime complexity is O(n^2).

To improve on it, notice that when we fix one of the integers ‘curValue’, we know the value of the other integer we need to find ( target - curValue ).
Then it becomes a simple search problem. You can store all the integers of the array in a hashmap and do a lookup to check if the elements exists in the map.'''




class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        list={}
        for i,v in enumerate(A):
            if B-v in list :
                return list[B-v]+1,i+1
            elif v not in  list :
                list[v]=i
        return []
                
