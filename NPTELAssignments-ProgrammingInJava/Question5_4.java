//Prefixed Fixed Code:
import java.util.*;
public class Question5_4{
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in); 
      int length = sc.nextInt(); 
      // create an array to save user input 
      int[] name = new int[length];
      int sum=0;//save the total sum of the array.
   try{
       for(int i=0;i<length;i++){  
          int userInput=sc.nextInt();
          name[i] = userInput;
          sum=sum+name[i]; 
          } 
        System.out.println(sum);
        }
       catch(InputMismatchException e) {
        System.out.println("You entered bad data.");
        }
 }
}
