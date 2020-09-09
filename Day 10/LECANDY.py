''' PROBLEM STATEMENT TAKEN FROM : https://www.codechef.com/problems/LECANDY
    Terminologies Used           : test_cases for the number of test cases
                                   count_elephants for the total number of elephants in jungle
                                   count_candies for the total number of candies
                                   candies_distribution_demo is an array that has the distribution of candies among several elephants
    Approach Used for problem    : Clearly if A[i] denotes the candies distributed to ith elephant then at most A[1] + A[2] + A[3] ........A[n]
    <= count_candies(Reason candies distributed cannot be greater than total candies present
    Output format                : YES/NO'''

def isElephantHappy(count_elephants,count_candies,candies_distribution):
    n = len(candies_distribution)
    total_candies_distributed = 0 
    for i in range(n): 
        total_candies_distributed = total_candies_distributed + candies_distribution[i]
    # Case where total candies distributed are less than total number of candies, clearly that would be a fair distribution so printing YES in that
    # case
    if total_candies_distributed <= count_candies: 
        print('YES')
    # Case where total candies distributed are more than total number of candies present , that would be an unfair distribution so print NO
    else:  
        print('NO')

# One of the sample inputs taken from codechef
count_elephants_demo         = 4
count_candies_demo           = 6
candies_distribution_demo    = [2,1,1,3]
isElephantHappy(count_candies_demo,count_candies_demo,candies_distribution_demo)

# Code ends here