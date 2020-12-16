# Top-down Recursive function to find all possible combinations of words formed
# from mobile keypad
def findCombinations(keypad, input, index, res=""):
 
    # if we have processed every digit of key, print result
    if index == -1:
        print(res, end=' ')
        return
 
    # stores current digit
    digit = input[index]
 
    # size of the list corresponding to current digit
    length = len(keypad[digit])
 
    # one by one replace the digit with each character in the corresponding
    # list and recur for next digit
    for i in range(length):
        findCombinations(keypad, input, index - 1, keypad[digit][i] + res)
 
 
if __name__ == '__main__':
 
    keypad = [
        # 0 and 1 digit don't have any characters associated
        [],
        [],
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I'],
        ['J', 'K', 'L'],
        ['M', 'N', 'O'],
        ['P', 'Q', 'R', 'S'],
        ['T', 'U', 'V'],
        ['W', 'X', 'Y', 'Z']
    ]
 
    # input number in the form of a list (number can't start from 0 or 1)
    input = [2, 3, 4]
 
    # find all combinations
    findCombinations(keypad, input, len(input) - 1)
 


