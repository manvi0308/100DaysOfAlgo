''' The memoized program for a problem is similar to the recursive version with 
a small modification that it looks into a lookup table before computing solutions.
We initialize a lookup array with all initial values as NIL. Whenever we need the
solution to a subproblem, we first look into the lookup table. If the precomputed 
value is there then we return that value, otherwise, we calculate the value and 
put the result in the lookup table so that it can be reused later.'''

# Fibonacci program using the concept of memoization
def fib(num, lookup_table):
    
    if num == 0 or num == 1:
        lookup_table[num] = num
    
    if lookup_table[num] is None:
        lookup_table[num] = fib(num - 1, lookup_table) + fib(num - 2, lookup_table)
    
    return lookup_table[num]


# Driver program to test the above function 
def main(): 
    n = 5
    # Declaration of lookup table 
    # Handles till n = 100  
    lookup = [None]*(101) 
    print("Fibonacci Number is ", fib(n, lookup) )
  
if __name__=="__main__": 
    main() 
  
