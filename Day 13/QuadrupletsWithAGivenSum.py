'''Four sum problem : Quadruplets with given sum
   Useful links     : 'https://www.w3schools.com/python/ref_dictionary_setdefault.asp'
                      'https://github.com/manvi0308/100-Days-of-Python' (for code with complete details)
   Pre-requisites   : Dictionary and Hashing basics
   Logic            : Iterate through pair find its sum , subtract it from the desired sum if there exists a value in dictionary that equals the
                      value of remaining sum in that case a quadruplet will be found(i.e. array[i]+array[j]+array[k]+array[y] == sum
                      If after going through all pairs no quadruplets is found in that case return False'''

def quadrupletsWithGivenSum(array, size, desired_sum):

    # Creating an empty dictionary for the sake of storing values
    # Dictionary -> Keys : Sum of pair of elements of in list
    # Dictionary -> Values : Indexes of that pair
    dictionary = {}
    for i in range(size - 1):
        for j in range(i+1 , size): #The second loop starts from i = 1 in first iteration and goes upto the last element
            remaining_sum = desired_sum - (array[i] + array[j])
            
            # if there exists a value with remaining sum in dictionary
            if remaining_sum in dictionary:
                for pair in dictionary[remaining_sum]:
                    x, y = pair # Assign the value of that indices to x and y

                    # Checking for duplicacy i.e. where quadruplets don't overlap
                    if(x != i and x != j) and (y != i and y != j):
                        print('Quadruplets Found ',(array[i],array[j],array[x],array[y]))
                        return True
            
            # Inserting the current pair into the dictionary
            dictionary.setdefault(array[i]+array[j],[]).append((i,j))
    
    # Case where quadruplets is not found
    return False

# Driver code
if __name__ == '__main__':
    array_sample = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    desired_sum_sample = 34
    if not quadrupletsWithGivenSum(array_sample, len(array_sample), desired_sum_sample):
        print('Ooops!! Quadruplets do not exist')
        
