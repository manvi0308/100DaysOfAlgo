''' Problem Description

Given an integer array A of size N consisting of unique integers from 1 to N. You can swap any two integers atmost B times.
Return the largest lexicographical value array that can be created by executing atmost B swaps.

Approach : The key point is to observe the answer. If we have B swaps, what does the starting of the permutation look like?
The permutation starts with N for sure and continues with (n-1), (n-2), …, (n-B+1).
The best permutation we can make by making B swaps is by putting the B largest elements at the begining of the permutation in decreasing order.
We can simply store the index of each element in an auxillary array let’s say idx and with each iteration if at ith position, A[i] = N-i (i stating from 0)then we
need not to swap that value, else make a swap and update the index array(idx) accordingly.
Do this atmost B times, if there are no more swaps return the largest array till now.'''




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

