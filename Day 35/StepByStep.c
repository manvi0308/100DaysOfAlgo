/* If target is negative, we can take it as positive because we start from 0 in symmetrical way.
Idea is to move in one direction as long as possible, this will give minimum moves. Starting at 0 first move takes us to 1, second move takes us to 3 (1+2) position, third move takes us to 6 (1+2+3) position, ans so on;
So for finding target we keep on adding moves until we find the nth move such that 1+2+3+…+n>=target.

Keep adding sum = 1 + 2 + .. + n >= target. Solving this quadratic equation gives the smallest n such that sum >= target, i.e solving for n in n(n+1) / 2 – target >= 0 gives smallest n.
If sum == target, answer is n. Now next case where sum is greater than target. Find the difference by how much steps index is ahead of target, i.e sum – target.

Case 1 : Difference is even then answer is n, (because there will always a move flipping which will lead to target).
Case 2 : Difference is odd, then take one more step, i.e add n+1 to sum and now again take the difference. If difference is even the n+1 is the answer else take one more move and this will certainly make the difference even then answer will be n + 2.

Explanation : Since difference is odd. Target is either odd or even.
case 1 : n is even (1 + 2 + 3 + … + n), then adding n + 1 makes the difference even.
case 2 : n is odd then adding n + 1 doesn’t makes difference even so take one more move, i.e., n+2.*/

/**
 * @input A : Integer
 * 
 * @Output Integer
 */
int solve(int A) {
    
    // If initial position is the same as final position
    if(A == 0) 
        return 0;
    
    // If final position is behind/Negative side of initial position
    if (A < 0) 
        
        A = -1 * A; // Taking the absolute value , since we are concerned about the number of 
        // moves
    
    // main approach begins here    
    int n = 1;
    
    // calculating the value of minimum value of moves required to reach or cross the
    // target
    
    while ((n * (n + 1))/2 < A) 
        n += 1;
        
    long long int x = (n * (n+1))/2;
    long long int y = ((n+2) * (n+1))/2;

    
    if((x-A)%2==0) 
        return n;
    
    if((y-A)%2==0) 
        return n+1;
    
    return n+2;
}
