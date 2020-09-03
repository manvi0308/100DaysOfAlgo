# Problem Statement: For a given list , find triplets with a given/desired sum
''' To Know Points: 1) List is not sorted
                    2) Can have both positives and negatives
                    3) Solve better than  O(n^3) complexity'''

def findTriplets(list , desired_sum):
    new_list = sorted(list)
    n = len(new_list)
    found = False

    for i in range(n):
        l = i+1
        r = n-1
        x = new_list[i]

        if (x + new_list[l] + new_list[r] == sum):
            print(x , new_list[l] , new_list[r])
            l += 1
            r -= 1
            found = True

        elif(x + new_list[l] + new_list[r] < sum):
            l += 1
        
        else:
            r -= 1
    if(found == False):
        print('No such triplets found')


arr = [0 ,-1 ,2 ,-3 ,1]
sum = 0
findTriplets(arr , sum)
        