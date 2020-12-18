

# DP function to find total ways to reach the n'th stair from bottom
# when a person is allowed to climb either 1 or 2 or 3 stairs at a time
def totalWays(n):
 
    # create a list of n+1 size for storing solutions to the sub-problems
    lookup = [None] * (n + 1)
 
    # base case: 1 way (with no steps)
    lookup[0] = 1
 
    # There is only 1 way to reach the 1st stair
    lookup[1] = 1
 
    # There are 2 ways to reach the 2nd stair
    lookup[2] = 2
 
    # Fill the lookup table in bottom-up manner
    for i in range(3, n + 1):
        lookup[i] = lookup[i - 1] + lookup[i - 2] + lookup[i - 3]
 
    return lookup[n]
 
 
if __name__ == '__main__':
 
    n = 4
    print("Total ways to reach the " + str(n) + "'th stair are", totalWays(n))
 


