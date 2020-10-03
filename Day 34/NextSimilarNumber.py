''' Problem Description:-  Given a number A in a form of string.
You have to find the smallest number that has same set of digits as A and is greater than A.

If A is the greatest possible number with its set of digits, then return -1.

Constraints: 1 <= A <= 10^100000
A doesn't contain leading zeroes.

Approach: Following are few observations about the next greater number.

If all digits sorted in descending order, then output is always “Not Possible”. For example, 4321.
If all digits are sorted in ascending order, then we need to swap last two digits. For example, 1234.
For other cases, we need to process the number from rightmost side (why? because we need to find the smallest of all greater numbers)
You can now try developing an algorithm yourself.

Following is the algorithm for finding the next greater number.

Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than the previously traversed digit. For example, if the input number is “534976”, we stop at 4 because 4 is smaller than next digit 9. If we do not find such a digit, then output is “Not Possible”.

Now search the right side of above found digit ‘d’ for the smallest digit greater than ‘d’. For “534976″, the right side of 4 contains “976”. The smallest digit greater than 4 is 6.

Swap the above found two digits, we get 536974 in above example.

Now sort all digits from position next to ‘d’ to the end of number. The number that we get after sorting is the output. For above example, we sort digits in bold 536974. We get “536479” which is the next greater number for input 534976.

The above implementation can be optimized in following ways.

We can use binary search in step II instead of linear search.
In step 4, instead of doing simple sort, we can apply some clever technique to do it in linear time. Hint: We know that all digits are linearly sorted in reverse order except one digit which was swapped.
With above optimizations, we can say that the time complexity of this method is O(len(A)).

'''


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        for i in range(len(A)-2, -1, -1):
            last_number = sorted(A[i:])
            for j in range(len(last_number)):
                m = int(A[:i] + last_number[j] + ''.join(last_number[:j] + last_number[j+1:]))
                if m > int(A):
                    return m
