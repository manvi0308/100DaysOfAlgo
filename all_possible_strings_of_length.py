# Problem statement: Print all possible strings of length k that can be formed from a set of n charactersFor a length k ,set of size n n^k 
# strings can be formed
''' Approach is to start with a string which is empty/blank ,add all characters to that empty string ,
for every character added print all possible string with current character by recursive calling'''
def printAllStringsOfLengthk(set , k): # This method is mainly a wrapper over recursive function 
    length_set = len(set)
    printAllStringsOfLengthkRec(set , " ", length_set, k)

''' The main recursive method'''
printAllStringsOfLengthkRec(set ,prefix  ,length_set ,k):
    if(k==0): #Base case where k is zero print prefix
        print(prefix) 
        return
    for i in range(length_set):
         newPrefix = prefix + set[i] #In thiis line adding the next character of input
         printAllStringsOfLengthkRec(set , newPrefix ,length_set ,k - 1)

# Driver code
if __name__ == '__main__':

    print('First Sample Test')  #Sample test 1
    set1 = ['a', 'b', 'c']
    k = 4
    printAllStringsOfLengthk(set1 , k)

    print('\n Second Test')  #For sample test 2
    set2 = ['m','a','n','v','i']
    k = 2
    printAllStringsOfLengthk(set2 , k)

# Code ends here

