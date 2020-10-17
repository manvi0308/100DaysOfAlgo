def countWaysUtil(n, m): 
    # Creates list res with all elements 0 
    res = [0 for x in range(n)]  
    res[0], res[1] = 1, 1
      
    for i in range(2, n): 
        j = 1
        while j<= m and j<= i: 
            res[i] = res[i] + res[i-j] 
            j = j + 1 
    return res[n-1] 
  
# Returns number of ways to reach s'th stair 
def countWays(s, m): 
    return countWaysUtil(s + 1, m) 
      
# Driver Program 
s, m = 4, 2
print "Number of ways =", countWays(s, m) 
      
