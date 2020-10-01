'''

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

'''

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

# Generating all prime numbers between 1 to 1million
primes = primes(1000000)

# length of the consecutive prime sum
length = 0

# value of the consecutive prime sum
largest = 0

# max value of the j variable(second for loop)
lastj = len(primes)

# two for loops
for i in range(lastj):
    for j in range(i+length, lastj):
        sol = sum(primes[i:j])
        if sol < 1000000:
            if sol in primes:
                length = j-i
                largest = sol
        else:
            lastj = j+1
            break

# printing the requried solution
print (largest)
