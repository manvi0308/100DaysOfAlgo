'''Problem Statement     : Count substrings  that starts and ends with same letter
   Mathematical Brokedown: Clearly in any string say 'manvi',number of substrings ending with a particular alphabet will be (frequency
   of that alphabet + 1)Cto the base 2 i.e. in combination formula nCr n will be frequency of that alphabet + 1 and r 
   will always be 2[Used the approach of combionatrics and permutations]
   Time Complexity       : O(n)
   Space complexity      : O(1)
   Assumptions           : Only lower case alphabets are there'''

MAX_CHARACTERS = 26
# A function that will count the frequency of each character
def countSubstringsWithSameEnding(s):
    result = 0
    n = len(s)
    count = [0]*MAX_CHARACTERS
    
    for i in range(n):
        count[ord(s[i]) - ord('a')] += 1

    # Computation of result
    for i in range(MAX_CHARACTERS):
        result += (count[i] *(count[i]+1)/2)
    return result

# Sample inputs
string_input = 'companion'
print(countSubstringsWithSameEnding(string_input))
