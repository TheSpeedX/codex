class problem17
{
   public static String[] ones = 
   { "","one","two","three","four","five","six","seven","eight","nine","ten",
      "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"};

   public static String[] tens = 
   {"","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"};

   public static String[] hundreds = 
   {"","onehundred","twohundred","threehundred","fourhundred","fivehundred","sixhundred",
      "sevenhundred","eighthundred","ninehundred"}; 

    public String word(int arg)
   {
      String withAnd = "";

      if(arg == 1000)
      {
         return "onethousand";
      }

      if(arg < 20)
      {
         return ones[arg];
      }

      if(arg < 100)
      {
             //divided arg by 10 gives it the correct index position in the array of tens
             //example: 80 is at position 8 in the tens array
             //80/10 = 8. tens[8] = "eighty"
         return tens[arg/10] + word(arg%10);
      }

         // if the number is not an even hundred value i.e 100, 200, 300
         // then you have to add and to it according to the problem specs
         //getting the remainder when divided by 100 allows you to see
         //if the number needs an and
         // ex: 124 % 100 = 24, so the answer would be onehundredandtwentyfour
      withAnd = word(arg % 100);

      if(withAnd.length() > 0)
         withAnd = "and" + withAnd;

         return hundreds[arg/100] + withAnd;
   }//end word

     public int letterCt(int arg)
     {
        //  System.out.println(word(arg));
        //  System.out.println(word(arg).length());
         return word(arg).length();
     }

     public static void main(String[] args)
     {
         int result = 0;

         for(int i = 1; i <= 1000; i++)
         {
            //  System.out.println("numWord: " + i);
             result += new problem17().letterCt(i);
         }

         System.out.println("Result: " + result);
     }//end main
}//end 