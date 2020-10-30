//Complete the following code fragment to read three integer values from the keyboard and find the sumof the values.
 //Declare a variable "sum" of type int and store the result in it.
 
 // Write the appropriate statement(s) to import the package(s) you need in your program
import java.util.*;
public class Question1{ 
        public static void main (String[] args){

//Write the appropriate code to read the 3 integer values and find their sum.
  int a,b,c,sum;
          Scanner s = new Scanner(System.in);
          a = s.nextInt();
          b = s.nextInt();
          c = s.nextInt();
          sum = a+b+c;
 System.out.println(sum);
  }
}