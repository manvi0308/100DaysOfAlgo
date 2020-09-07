'''Problem Statement: Given a binary String with wildcard characters('?') at some places.Print all the possible binary strings
combinations formed by replacing wildcard characters with 0 or 1
Approach            : Recursive and Backtracking
Point to Consider   : For a string with n wildcard characters , 2^n unique combination could be there of 0s and 1s so total
2^n strings will be formed after replacing wildcard characters with 0 and 1
Example             : 1?1 ,possible strings could be 101 and 111 
Mathematical Concept involved : Permutations and Combinations'''


def printBinaryStrings(str , i = 0):

    if i == len(str):
        print(''.join(str))
        return
    # in case the current character is a wildcard character
    if str[i] == '?':
        for character in '01':
            str[i] = character #Replace it with either 0 and 1
            printBinaryStrings(str,i+1) #recur for remaining pattern/string
            str[i] = '?' # backtracking
    # if the current character is 0 or 1 you can safely ignore it and then recur for remaining pattern
    else:
        printBinaryStrings(str, i+1) 

# Code execution begins here   
if __name__ == '__main__':
    pattern = '11??01??110'  
    printBinaryStrings(list(pattern))
