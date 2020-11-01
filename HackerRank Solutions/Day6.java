/*Given a string,S, of length N that is indexed from  0 to N-1, print its even-indexed and odd-indexed 
characters as  space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.
*/
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        in.nextLine();
        for(int i = 0; i<N; i++)
        {
            String string = in.nextLine();
            char[] charArray = string.toCharArray();
            for(int j =0;j<charArray.length;j++)
            {
              if(j%2==0)
              {
                System.out.print(charArray[j]);
              }
            }
            System.out.print(" ");
            for(int j = 0;j<charArray.length;j++)
            {
              if(j%2 != 0)
              {
                System.out.print(charArray[j]);
              }
            }
            System.out.println();
        }
        in.close();

           }
}
