# Problem Statement : Given a list find triplets with given sum
# This approach is naive and complexity is o(n^3)
def triplets_with_given_sum(list , sum):
    print('Desired sum is : ' +str(sum))
    n = len(list)
    Found = False
    for i in range(0 ,n-2):
        for j in range(i+1 ,n-1):
            for k in range(i+2 , n):
                if( list[i]+ list[j] +list[k] == sum):
                    Found = True
                    print('Triplets found at position of first number '+ str(i)+ ' Second number position ' + str(j) + ' Third number position '  +str(k))
                    print(list[i] ,list[j] ,list[k])
    
    if Found == False:
        print('Triplets do Not Exist with given sum')
    else:
        print('Matching Pair Found')


    

arr = [0 ,-1 ,2 ,-3 ,1]
sum = 0
triplets_with_given_sum(arr , sum)
