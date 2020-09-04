# Problem statement: To print all the permutation of a given string
'''Note that a string of length n will have n factorial permutable strings
Similarly in backtracking tree /approach the height or depth of tree will be equal to the length of string
Algorithm: 1)Fix one charcter(maybe A) and swap the rest of characters
           2) Call the function recursively
           3) Go for backtracking and do swapping again'''
# A recursive function that will generate permutations of a given target string
def generatePermutationsOfStrings(string , start , end): 
    current = 0 # A variable that will point to the current position
    
    if(start == end-1): #Base case where the length of string is only 1 character
        print(string) #The only permutation possible will be the string itself
    
    else:
        for current in range(start , end):
            x = list(string)
            #Now we will swap the list by fixing a charcter
            temp = x[start]
            x[start] = x[current]
            x[current] = temp
            # now recursively callling the same function for rest of characters
            generatePermutationsOfStrings("".join(x),start+1,end);
            temp = x[start]
            x[start] = x[current]
            x[current] = temp

str = 'MANVI'
n = len(str)
generatePermutationsOfStrings(str , 0, n)
