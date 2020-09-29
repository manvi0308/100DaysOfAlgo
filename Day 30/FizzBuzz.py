/* Given a positive integer A, return an array of strings with all the integers from 1 to N.
But for multiples of 3 the array should have “Fizz” instead of the number.
For the multiples of 5, the array should have “Buzz” instead of the number.
For numbers which are multiple of 3 and 5 both, the array should have “FizzBuzz” instead of the number.

Approach: While Iterating from 1 to N, you need to check the following conditions in sequence:

 1) Check whether the number is divisible by 3 and 5, if that is the case, print FizzBuzz.
 2) Check whether the number is divisible by 3, in that case, print Fizz.
 3) Next, check whether the number is divisible by 5, in that case print Buzz.
 4) Otherwise, print the number.

Time Complexity: O(N)
Space Complexity: O(1)*/

class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        output = []
        if A <= 0: return output
        for i in range(1, A+1):
            
            if i % 3 == 0:
                if i % 5 == 0:
                    output.append('FizzBuzz')
                else:
                    output.append('Fizz')
            elif i % 5 == 0:
                output.append('Buzz')
            else:
                output.append(i)
        return output
