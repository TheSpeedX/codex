import java.math.BigInteger;

class problem16 {
 public static void main(String[]args){
  BigInteger mul=new BigInteger("1");
  BigInteger bg=new BigInteger("2");
  
  for (int i = 0; i < 1000; i++) {
   mul=mul.multiply(bg);
  }
  
  int sum=0;
  String text=mul.toString();
  for (int i = 0; i < text.length(); i++) {
   sum+=Integer.parseInt(new Character(text.charAt(i)).toString());
  }
  System.out.println(sum);
 }
}