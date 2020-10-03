''' Problem Description
Given a positive integer A, return its corresponding column title as appear in an Excel sheet.

Problem Constraints
1 <= A <= 1000000000

Input Format
First and only argument is integer A.

Output Format
Return a string, the answer to the problem.

Approach: base conversion'''

class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        
        # chr -> integer to character
        # ord -> character to integer
        
        # creating a list n[] that contains ASCII values of characters A - Z
        n=[chr(i) for i in range(ord("A"),ord("Z")+1)]
        
        # .insert(position, element)
        n.insert(0,0)
        
        # creating two empty lists
        a=[];p=[]
        
        # typical base conversion 
        while A>26:
            k=A%26
            A=A//26
            if k==0:
                a.append(26)
                A-=1
            else:
                a.append(k)
                
        a.append(int(A))
        a.reverse()
        for i in a:
            p.append(n[i])
            r="".join(p)
        return r
