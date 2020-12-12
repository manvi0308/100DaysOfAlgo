'''Problem Description

Given an integer array A of size N consisting of unique integers from 1 to N. You can swap any two integers atmost B times.

Return the largest lexicographical value array that can be created by executing atmost B swaps.



Problem Constraints
1 <= N <= 106

1 <= B <= 109 '''




import heapq

def solution(a,b):
    n=len(a)
    c=[-t for t in a]
    heapq.heapify(c)
    
    pos=[-1 for _ in range(n)]
    for i in range(n):
        pos[a[i]-1]=i
    # print(pos)
    i=0
    cnt=1
    while cnt<=b:
        if len(c)==0:
            break
        temp=-heapq.heappop(c)
        # print(temp)
        # print(pos,a)
        
        if a[i]!=temp:
            kt=a[i]
            a[pos[temp-1]]=a[i]
            a[i]=temp
            
            pos[kt-1]=pos[temp-1]
            pos[temp-1]=i
            cnt+=1
        i+=1
            
    
    return a

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        return solution(A,B)

