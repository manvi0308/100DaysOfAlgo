# Program for Array Rotation
'''Problem Statement : Write a function that rotates an arr[] of size n by d elements in right direction
Time complexity is O(n) and space complexity is O(1)'''
def leftRotate(arr ,d , n):
    for i in range(gcd(d , n)):
    #move ith values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j+d
            if k>=n:
                k = k-n
            if k==1:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
# Utility function to print an arrray
def printArray(arr , size):
    for i in range(size):
        print(arr[i] ,end = '')

def gcd(a , b):
    if b == 0:
        return a
    else:
        return gcd(b ,a%b)
# Driver program
arr = [7 ,45 ,3 ,12 ,56 ,13]
leftRotate(arr ,3 ,6)
printArray(arr, 7)