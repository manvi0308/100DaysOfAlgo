''' Problem Statement: Check if two numbers are coprime or not
    Approach : Two numbers are coprime if their GCD is 1
    Also Case 1: When two numbers are equal
         Case 2: When either of two numbers are zero
         Case 3: When one of number is greater than other gcd(x,y) == gcd(x-y,y)[simple mathematical property],
         provided x > y
    '''
# Function to return gcd of a and b
def __gcd(x, y):
    if(x == y): # Case 1
        return x
    
    if(x == 0 or y == 0): # Case 2
        return 0
    
    if(x > y): # Case 3: when x > y
        return __gcd(x-y ,y)
    
    return __gcd(x ,y-x)

def coprime(x , y):
    if(__gcd(x, y) == 1):
        print('They are coprime numbers')
    else:
        print('Not Coprime numbers')
# Sample Inputs
num1 = 14
num2 = 21
coprime(num1 , num2)
num3 = 4
num4 = 5
coprime(num3 , num4)
    