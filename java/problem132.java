int result = 0;
int count = 0;
int[] primes = Sieve(2, 200000);
int k = (int) Math.Pow(10, 9);
int i = 0;
 
while(count < 40){
    if (BigInteger.ModPow(10, k, 9 * primes[i]) == 1) {
        count++;
        result += primes[i];
    }
    i++;
}
