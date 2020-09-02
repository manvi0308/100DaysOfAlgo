# Problem statement : Print all the permutation in lexicographical/dictionary maner
# Start by sorting the strings


# Below is the functional implementation of lexicographic permutation where repetition of characters is allowed
def lexicographicalpermutation(str , res = ' '):

    # base condition(permutation found)
    if len(res) == len(str):
        print(res , end = ' ') #In this case simply print permutation and then return
        return
    
    # Considering ach character one by one
    for c in str:
        lexicographicalpermutation(str , res+c)


if __name__ == '__main__':

    str = 'XYZ'
    # Sorting so as to get lexicographical prder
    c = sorted(list(str))

    lexicographicalpermutation(c)
