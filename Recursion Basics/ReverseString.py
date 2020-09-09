# Print a string in reverse order

string  =  'manvi'

def reverseStringUsingRecursion(str):
    if len(str) == 0:
        return str
    
    else:
        return reverseStringUsingRecursion(str[1:]) + str[0]


print(reverseStringUsingRecursion(string))
