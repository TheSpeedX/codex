import java.util.*; 
import java.io.*;
import java.util.Scanner;
  
class Main { 
    static int factorial(int n) 
    { 
        int fact = 1; 
        while (n != 0) { 
            fact = fact * n; 
            n--; 
        } 
        return fact; 
    } 
  
    static boolean isKrishnamurthy(int n) 
    { 
        int sum = 0; 
  
        int temp = n; 
        while (temp != 0) { 

            sum += factorial(temp % 10); 
  
 
            temp = temp / 10; 
        } 

        return (sum == n); 
    } 
  
 
    public static void main(String[] args) 
    { 
        Scanner sc=new Scanner(System.in);
        int n =sc.nextInt(); 
        if(n==1 || n==2)
            System.out.println(n+" is not a curious number"); 
        else if(isKrishnamurthy(n)) 
            System.out.println(n+" is a curious number"); 
        else
            System.out.println(n+" is not a curious number"); 
    } 
} 
