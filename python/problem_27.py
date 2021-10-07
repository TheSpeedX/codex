import prime

max_pair = (0,0,0)
for a in xrange(-999, 1000):
    for b in xrange(max(2, 1-a), 1000): # b >= 2, a + b + 1 >= 2
        n, count = 0, 0
        while True:
            v = n*n + a*n + b
            prime._refresh(v)
            if prime.isprime(v): count = count + 1
            else: break
            n = n + 1
        if count > max_pair[2]:
            max_pair = (a,b,count)

print max_pair[0] * max_pair[1]
