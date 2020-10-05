''' Problem Statement : A rainbow array of n elements follows the form

{ 1 (repeated a1 times), 2 (a2 times), 3 (a3 times), 4 (a4 times), 5 (a5 times), 6 (a6 times), 7 (a7 times), 6 (a6 times), 5 (a5 times), 4 (a4 times), 3 (a3 times), 2 (a2 times), 1 (a1 times) 

Given an array consisting of n elements, check if it’s a rainbow array or not.

Problem Link: https://www.codechef.com/problems/RAINBOWA
'''

for i in range(int(input())):
        x=int(input())
        y=list(map(int,input().split()))
        s={1,2,3,4,5,6,7}
        if y==y[::-1] and set(y)==s:
            print('yes')
        else:
            print('no')
       
