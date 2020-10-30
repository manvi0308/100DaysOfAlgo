//to chech whether number is armstrong or not

import java.util.Scanner;
public class Exercise1_4 {
    public static void main(String[] args) {
	   Scanner sc = new Scanner(System.in);
	   int n=sc.nextInt();
           int result=0;
int temp=n;
int c=0,t; 
//Use while loop to check the number is Armstrong or not.
    while(n>0)
	{
		t=n%10;
		n=n/10;
		c=c+(t*t*t);
	}		
	if(temp==c)
		result=1;
	else
		result=0;
    //Evaluation code 
    System.out.println(result);
 }
}
