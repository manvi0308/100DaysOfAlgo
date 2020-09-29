/* Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer
Approach: Lets say g is gcd(m, n) and m > n.

m = g * m1
n = g * m2

m - n = g * (m1 - m2)

gcd (m, n) = gcd(m-n, n)

           = gcd(m - 2n, n) if m >= 2n
           = gcd(m - 3n, n) if m >= 3n 
             .
             .
             .
           = gcd(m - k*n, n) if m >= k*n
           
       In other words, we keep subtracting n till the result is greater than 0. Ultimately we will end up with m % n.
       
              So gcd(m, n)  = gcd(m % n, n) .*/
              
   class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
    
        if A < B:
            A, B = B, A
        
        while B:
            A, B = B, A % B
        
        return A
