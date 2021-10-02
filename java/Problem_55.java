import java.math.BigInteger;

 class Number {
	public static void main(String[] args) {
		long count = 0;
		for (long i = 1; i < 10000; i++) {
			if (isLychrelNumber(i)) {
				count++;
			}					
		}
		System.out.println(count);
	}

	private static boolean isLychrelNumber(long number) {
		BigInteger next = BigInteger.valueOf(number);
		int numIterations = 1;
		do {
			next = next.add(new BigInteger(
					new StringBuffer(next.toString()).reverse().toString()));
			if (isPalindrome(next.toString())) {
				return false;
			}
			numIterations++;
		}
		while (numIterations <= 50);
		return true;
	}	
	
	private static boolean isPalindrome(String word) {
		int length = word.length();
		for (int i = 0; i < length/2; i++) {
			if (word.charAt(i) != word.charAt(length-1-i)) {
				return false;
			}
		}
		return true;
	}
}
