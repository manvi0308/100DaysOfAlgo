import java.util.Scanner;
  
  public class Question5_3 {
  public static void main(String[] args) { 
      int a, b;
      Scanner input = new Scanner(System.in);

       int result;  
       a = input.nextInt();
       b = input.nextInt();
  
      // try block to divide two numbers and display the result
         try {
              result = a/b;
              System.out.println(result);
     	     }
          // catch block to catch the ArithmeticException
          catch (ArithmeticException e) {
             System.out.println("Exception caught: Division by zero.");
          }

 }
}
