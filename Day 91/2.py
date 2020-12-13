''' Given n points on a 2D plane, find the maximum number of points that lie on the same straight line

Corner cases :

1) Have you handled overlapping points ?
2) Have you handled negative points for the same slope ? Like (0,0), (1,1) and (-1, -1)
3) Did you make sure that there are no divisions by 0 ? Like (1, 0), (1,4), (1, -1)
4) How do you handle when one of the differences in x and y is 0, and the other difference is negative / positive ? Like (4, -4), (8, -4), (-4, -4)'''




class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        n = len(A)
        if (n<=2):
            return n
        m = 0 #result value
        for i in range(n):
            l = {}  #every time reset the dict
            dup = 1 #count the duplicates
            for j in range(n):
                if (A[i]==A[j] and B[i]==B[j] and i!=j):        
                    dup+=1  #count duplicates
                elif i!=j :
                    if (A[i]==A[j]):  #vertical line
                        l['v'] = l.get('v',0) + 1
                    elif (B[i]==B[j]): # horizontal line
                        l['h'] = l.get('h',0) + 1
                    else:   #regular slope
                        slope = 1.0*(B[i]-B[j])/(A[i]-A[j])
                        l[slope] = l.get(slope,0)+1
            if (len(l)>0): 
                m = max(m,max(l.values())+dup)
            else: #if all points are duplicates, l is empty.
                m = max(m,dup)
        return m
