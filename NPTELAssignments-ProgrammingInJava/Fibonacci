import java.util.Scanner; //This package for reading input
public class Fibonacci { 
    
    public static void main(String args[]) { 
	 Scanner sc = new Scanner(System.in);
	 int n=sc.nextInt(); //Read an integer
        System.out.println(fib(n)); //Generate and print the n-th Fibonacci                
                                     //number
    } 
 static int fib(int n) {

        if (n==1)      //Terminate condition
            return 0;
        else if(n==2)
            return 1; 			
        return fib(n - 1) + fib(n - 2); //Recursive call of function
}  
}