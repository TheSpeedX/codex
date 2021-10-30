from functools import reduce
import math

primes=set([2,3,5,7,11,13,17,19,23])
def isPrime(n):
    n=abs(n)
    if n in primes:
       return True
    if n<2:
       return False
    if n==2:
       return True
    if n%2==0:
       return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    primes.add(n)
    return True

def aFactors(n):
    if isPrime(n):
        return [1,n]
    return set(reduce(list.__add__,([i,n//i] for i in range(1,int(math.sqrt(n))+1) if n%i==0)))


count=0
number=12
while number<=1500000:
    p=number/2
    f=aFactors(p)
    triangles=[]
    pairs=[(i, int(p/i)) for i in f]
    add=triangles.append
    for i in pairs:
        mList=aFactors(i[0])
        pairsOfmc=[(k,int(i[0]/k)) for k in mList]
        for j in pairsOfmc:
            add((2*i[1]*i[0]-i[1]*i[1]*j[0],2*i[0]*i[1]-2*i[0]*j[1],2*i[0]*j[1]+i[1]*i[1]*j[0]-2*i[0]*i[1]))
    r=0
    while r<len(triangles):
        if any(triangles[r][i]<=0 for i in range(len(triangles[r]))):
            del triangles[r]
        else:
            l=list(triangles[r])
            l.sort()
            triangles[r]=tuple(l)
            r+=1
    trianglesFinal=list(set(triangles))
    for i in trianglesFinal:
        print(number, i)
    if len(trianglesFinal)==1:
        count+=1
    number+=2
    print(count)
