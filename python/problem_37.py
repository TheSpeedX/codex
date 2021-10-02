def isprime(n):
  
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n 
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True
 
def peel_left(i):
    
    x = list(str(i))
    for n in range(1, len(x)):
        y = x[n:]
        s = int(''.join(y))
        if isprime(s):
            continue
        else:
            return "False"
    return "True"
 
def peel_right(i):
    
    x = list(str(i))
    for n in range(1, len(x)):
        y = x[:(-n)]
        s = int(''.join(y))
        if isprime(s):
            continue
        else:
            return "False"
    return "True"
     
def main():
    
    L = []
    for i in range(10, 1000000):
        if isprime(i):
            if (peel_left(i) == "True") and (peel_right(i) == "True"):
                L.append(i)
            else:
                continue
        else:
            continue
    print "L = ", L
    print "Answer = ", sum(L)
 
if __name__ == '__main__':
    main()
