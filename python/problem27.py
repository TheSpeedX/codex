import time


def gen_prime(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] is True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    prime_set = set()
    for p in range(2, n+1):
        if prime[p] is True:
            prime_set.add(p)
    return prime_set


def main(A, B):
    prime_set = gen_prime(10**6)
    max_num_prime = 0
    coeff = 1
    for a in range(-A, A+1):
        for b in range(-B, B+1):
            n = 0
            while True:
                eqn = n**2 + a*n + b
                if eqn not in prime_set:
                    break
                n += 1
            if n > max_num_prime:
                max_num_prime = n
                coeff = a*b
    return coeff


start = time.time()
print(main(1000, 1000))
end = time.time()
print("It took {} s".format(end-start))

