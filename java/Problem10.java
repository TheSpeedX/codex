import java.util.*;
import java.io.*;

public class Main { 
  

    static boolean checkPrime(int numberToCheck) 
    { 
        if(numberToCheck == 1) { 
            return false; 
        } 
        for (int i = 2; i*i <= numberToCheck; i++) { 
            if (numberToCheck % i == 0) { 
                return false; 
            } 
        } 
        return true; 
    } 
  

    static int primeSum(int l, int r) 
    { 
        int sum = 0; 
        for (int i = r; i >= l; i--) { 
  
            // Check for prime 
            boolean isPrime = checkPrime(i); 
            if (isPrime) { 
  
                // Sum the prime number 
                sum = sum + i; 
            } 
        } 
        return sum; 
    } 

    public static void main(String[] args) 
    { 
        Scanner sc=new Scanner(System.in);
        int l = 0;
        int r=sc.nextInt();
  
        // Call the method with l and r 
        System.out.println("The sum of the primes below "+r+" is "+primeSum(l, r)); 
    } 
} 
