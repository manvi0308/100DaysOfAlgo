''' Problem Statement: Count Consonants in a string
Pre-requisites: ord method and ASCII Numbers
Approach Used: Recursive'''

def isConsonant(character):
    character = character.upper()
    return not(character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U') and ord(character) >= 65 and ord(character) <= 90

def countConsonants(string, n):
    if n == 1:
        return isConsonant(string[0])
    
    return countConsonants(string,n-1) + isConsonant(string[n-1])


string_input = 'abcdefeeio'
print(countConsonants(string_input,len(string_input)))