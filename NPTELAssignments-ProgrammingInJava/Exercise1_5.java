/*Complete the code segment to find the highest mark and average mark secured by Hari in "s" number of subjects.

*/



import java.util.Scanner;
public class Exercise1_5{
    public static void main(String[] args) {
	 Scanner input = new Scanner(System.in);
         double mark_avg;
         int result;
         int i;
         int s;
      //define size of array
       s = input.nextInt();
     //The array is defined "arr" and inserted marks into it of integer type.
      int[] arr = new int[s];   
      
	 for(i=0;i<arr.length;i++)
	  {
        	arr[i]=input.nextInt();
	  } 
 //initialise maximum element as first element of array.  
	   int max=arr[0];
           double sum=arr[0];  
	  //traverse array elements to get the current max
      for(i=1;i<arr.length;i++)
	  { 
         sum=sum+arr[i]; 
         if(arr[i]>max)
            max =arr[i];
	  }
	 
    //Store the highest mark in the variable max
   //Store average mark in avgMarks
    result=max;	
    mark_avg=sum/(arr.length);    
 //Evaluation code 
    System.out.println(result);
    System.out.println(mark_avg);
 }
}