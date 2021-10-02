import java.util.*; 
class problem20{ 

static ArrayList<Integer> v=new ArrayList<Integer>(); 
static void multiply(int x)  
{  
    int carry = 0;  
    int size = v.size();  
    for (int i = 0 ; i < size ; i++)  
    {  
        // Calculate res + prev carry  
        int res = carry + v.get(i) * x;  
  
        // updation at ith position  
        v.set(i,res % 10);  
        carry = res / 10;  
    }  
    while (carry != 0)  
    {  
        v.add(carry % 10);  
        carry /= 10;  
    }  
}  
  
// Returns sum of digits in n!  
static int findSumOfDigits(int n)  
{  
    v.add(1); // adds 1 to the end  
  
    // One by one multiply i to current vector  
    // and update the vector.  
    for (int i=1; i<=n; i++)  
        multiply(i);  
  
    // Find sum of digits in vector v[]  
    int sum = 0;  
    int size = v.size();  
    for (int i = 0 ; i < size ; i++)  
        sum += v.get(i);  
    return sum;  
}  
  
// Driver code  
public static void main(String[] args)  
{  
    int n = 100;  
    System.out.println(findSumOfDigits(n));  
}  
} 