'''Given a string and a pattern containing wildcard characters, write an efficient algorithm to check if input string
matches with wildcard pattern or not'''




# Recursive function to check if the input matches
# with a given wildcard pattern
def isMatch(str, n, pattern, m):
 
    # end of pattern is reached
    if m == len(pattern):
        # return true only if end of input is also reached
        return n == len(str)
 
    # if the input reaches its end, return when the
    # remaining characters in the pattern are all '*'
    if n == len(str):
        for i in range(m, len(pattern)):
            if pattern[i] != '*':
                return False
 
        return True
 
    # if current wildcard character is '?' or current character in
    # pattern is same as current character in the input String
    if pattern[m] == '?' or pattern[m] == str[n]:
        # move to next character in the pattern and the input String
        return isMatch(str, n + 1, pattern, m + 1)
 
    # if current wildcard character is '*'
    if pattern[m] == '*':
        # move to next character in the input or
        # ignore '*' and move to next character in the pattern
        return isMatch(str, n + 1, pattern, m) or isMatch(str, n, pattern, m + 1)
 
    # we reach here when current character in the pattern is not a
    # wildcard character and it doesn't matches with the current
    # character in the input String
    return False
 
 


