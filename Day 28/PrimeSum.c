// Problem Statement : https://www.interviewbit.com/problems/prime-sum/

// A utility Function to check whether a number is prime or not
int isprime(int a)
{
    int i;
    for(i=2;i<=sqrt(a);i++)
    {
        if(a%i==0)
            return 0;
    }
    return 1;
}


int* primesum(int A, int *len1) {
    
     *len1 = 2;
    int i=2;
    // dynamically allocating memory according to question requirements
    // Note memory is allocated only for 2 integers coz we only need to have 2 integers in the resultant array
    int *array_prime_sum = (int *)malloc(2*sizeof(int));
    for(i=2;i<=A/2;i++)
    {
        // checking for the prime condition
        if(isprime(i)&&isprime(A-i))
        {
            array_prime_sum[0] = i;
            array_prime_sum[1] = A-i;
            return array_prime_sum;
        }
        if(i!=2)
            i++;
        
    }
