''' Maximum sum subarray problem -Kadane's algorithm
Given an array find a subarray which has the maximum sum '''

def maxSubarrayProblem(array):
    max_so_far = 0
    max_ending_here = 0
    for i in array:
        max_ending_here = max_ending_here + i
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_ending_here, max_so_far)
    
    return max_so_far

if __name__ == '__main__':

    array_demo = [0, 3, 0, 8, 2, 0, -1, 14, 2, 4, 4]

    output = maxSubarrayProblem(array_demo)
    print('Maximum sum of subarray in the given array is : ',output )