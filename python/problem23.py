from math import sqrt
import time

start = time.time()


def divisors(n):
    divs = []
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            if i*i == n:
                divs.extend([i])
            else:
                divs.extend([i, n/i])
    return divs


ab = []


for i in range(12, 28123):
    if sum(divisors(i)) > i:
        ab.append(i)

non_ab = [x for x in range(28123)]

for i in range(len(ab)):
    for j in range(i, 28123):
        if ab[i] + ab[j] < 28123:
            non_ab[ab[i] + ab[j]] = 0
        else:
            break
print(sum(non_ab))
print(time.time() - start)

