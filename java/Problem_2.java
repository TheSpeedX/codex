/*
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

 */
public class Problem_2
 {

	public static void main(String[] args) 
               {
		
	       int x = 0;
	       int y = 1;
	       int z;
	       int max = 4000000 ;
	       int sum = 0;
	       for (z = 0; z < max; z++)
               {
	           
	           z = x + y;
	           x = y;
	           y = z;
	           
	           
	           if (z % 2 == 0) {sum += z;}
	       }
	       System.out.println(sum);

	}

}
