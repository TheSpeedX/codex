from math import sqrt
L = 11000
ds = [1]*L
for i in range(2, int(sqrt(L))):
    for j in range(i+1, L//i):
        ds[i*j]+= i+j
an = []
for i in range(2, L):
    if ds[i] < i and ds[ds[i]] == i: an+= [ds[i], i]
N = 10000
print("Amicable sum <",N,"=", sum(a for a in an if a<N))
