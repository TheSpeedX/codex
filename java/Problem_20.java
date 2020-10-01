import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt();
        while(T-- >0){
            long n=sc.nextLong();
            long position1=Math.round((-1+Math.sqrt(1+8*n))/2);
            long position2=Math.round(-1-Math.sqrt(1+8*n))/-2;
               long nthTerm=position1*(position1+1)/2;
                if(n==nthTerm){
                    System.out.println(position1);
                    continue;
                }
            nthTerm=position2*(position2+1)/2;
                if(n==nthTerm){
                    System.out.println(position2);
                }
            else{
            System.out.println("-1");    
            }
        }
    }
}
