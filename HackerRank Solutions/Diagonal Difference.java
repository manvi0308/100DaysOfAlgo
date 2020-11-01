import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int n;
        Scanner in=new Scanner(System.in);
        n=in.nextInt();
        int a[][]=new int[n][n];
        for(int i=0;i<n;i++){
        	for(int j=0;j<n;j++){
        		a[i][j]=in.nextInt();
        	}
        }
        int pd=0,npd=0;
        for(int i=0;i<n;i++){
        	for(int j=0;j<n;j++){
        		if(j==i)
        			pd=pd+a[i][j];
        	}
        }
        for(int i=0;i<n;i++){
        	for(int j=0;j<n;j++){
        		if(i==n-j-1){
        			npd=npd+a[i][j];
        		}
        	}
        }
        int dif=npd-pd;
        dif=Math.abs(dif);
        System.out.println(dif);
    }
}