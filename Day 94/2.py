# Python3 code to find the number 
# of ways to paint stairs 
  
# Function to find the number of ways 
def ways( n ): 
    W = list() 
      
    # take base case for 1 and 2 
    W.append(0) 
    W.append(2) 
    W.append(3) 
      
    i = 3
    while i <= n: 
        W.append(W[i - 1] + W[i - 2]) 
        i = i + 1
          
    return W[n] 
  
# Driver code 
n = 3
print(ways(n)) 
