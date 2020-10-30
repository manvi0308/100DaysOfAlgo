/*
Write a program which will print a pyramid of "" 's of height "n" and print the number of "" 's in the pyramid.

For example:

input : 5
output:  

        *  
      * * *
    * * * * * 
  * * * * * * *
* * * * * * * * * 
25*/
import java.util.*;
public class Pattern1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();//for the nu,br
        int k = 0,sum=0;
        for(int i = 1; i <= n; ++i, k = 0) {
            for(int space = 1; space <= n - i; ++space) {
                System.out.print("  ");
            }
            while(k != 2 * i - 1) {
                System.out.print("* ");
                sum=sum+1;
                ++k;
            }
            System.out.println();
        }
         System.out.println(sum); 
    }
}
