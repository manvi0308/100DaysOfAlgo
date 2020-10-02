import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    
    # a utility function that finds out gcd of two numbers
    def gcd(self, a, b):
        if(b == 0):
            return a
        
        return self.gcd(b, a % b)
        
    def cpFact(self, A, B):
        
        while(self.gcd(A,B) != 1):
            A = A/self.gcd(A,B)
        
        return int(A)
    
