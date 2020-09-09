/* Terminologies Used : test_cases for the number of test cases
                        elephant_count for the total number of elephants in jungle
                        candies_count for the total number of candies
                        a - an array that has the distribution of candies among several elephants
    Approach Used     : After taking all the inputs as given in the input format , make a new variable counter called as start,Now whenever a user give input for the array of candies
    distribution to elephant you will compare it with the total number of candies , if by any chance candies given to one elephant increases or is greater than total number of
    candies, program/distribution fails*/
          

#include <stdio.h>
int main(void)
{
 	int test_cases;  #for the test cases input
 	scanf("%d",&test_cases);
 	while(test_cases--)
 	{
 		int start = 0;
 		long long int elephant_count, candies_count;  #used long long coz of the input ranges
 		scanf("%lld %lld",&elephant_count, &candies_count);
 		int a[elephant_count];
 		for(int i=0;i<n;i++)
 		{
 			scanf("%lld",&a[i]);  #Taking user input for the candies distribution to elephants
 			if(a[i]<=candies_count)  #
 			{
 				candies_count = candies_count - a[i];
 				start++;
 			}
 		}
 		if(start<=elephant_count - 1)
 		printf("No\n");
 		else 
 		printf("Yes\n");
 	}
 	return 0;
 }
