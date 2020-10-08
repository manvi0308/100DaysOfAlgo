'''Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

    G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
    
 Approach: 1) Create a new empty stack st

2) Iterate over array `A`,
   where `i` goes from `0` to `size(A) - 1`.
    a) We are looking for value just smaller than `A[i]`. So keep popping from `st` till elements in `st.top() >= A[i]` or st becomes empty.
    b) If `st` is non empty, then the top element is our previous element. Else the previous element does not exist. 
    c) push `A[i]` onto st'''
    
    
 # Code
 class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, array):
        """ Time complexity: O(n). Space complexity: O(n), n is len(array).
        """
        stack = []
        result = []
        for num in array:
            # see of there's integer smaller than num in the stack
            while stack and stack[-1] >= num:
                stack.pop()
            if stack:  # found the smaller integer
                result.append(stack[-1])
            else:  # stack is empty, smaller integer wasn't found
                result.append(-1)
            stack.append(num)  # push current num to the stack
        return result
