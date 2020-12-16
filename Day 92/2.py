from collections import deque
 
 
# Recursive function to print all distinct subsets of S
# S   --> input set
# out --> list to store subset
# i   --> index of next element in set S to be processed
def findPowerSet(S, out, i):
 
    # if all elements are processed, print the current subset
    if i < 0:
        print(list(out))
        return
 
    # include current element in the current subset and recur
    out.append(S[i])
    findPowerSet(S, out, i - 1)
 
    # exclude current element in the current subset
    out.pop()       # backtrack
 
    # remove adjacent duplicate elements
    while i > 0 and S[i] == S[i - 1]:
        i = i - 1
 
    # exclude current element in the current subset and recur
    findPowerSet(S, out, i - 1)
 
 
# Program to generate all distinct subsets of given set
if __name__ == '__main__':
 
    S = [1, 3, 1]
 
    # sort the set
    S.sort()
 
    # create an empty list to store elements of a subset
    out = deque()
    findPowerSet(S, out, len(S) - 1)
 



