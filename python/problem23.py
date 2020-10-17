import itertools
import functools
import operator
from math import sqrt

def foo(a):
    d = 1
    z = 0
    while d <= sqrt(a):
        d += 1
        if a == 2:
            z = a
        elif (a % d) == 0:
            z = False
            break
        else:
            z = a

    return z

def bar(value):
    v = []
    d = 1
    value1 = value
    while d <= sqrt(value1):
        d += 1
        if foo(d) != False and value1 % d == 0:
            v.append(d)
            value1 = value1 / d
            d = 1
    if value1 != value and value1 != 1:
        v.append(value1)

    return v

def calculate_divisors(n):
    prime_multiples_list = bar(n)
    unique_combinations = set()
    for i in range(1, len(prime_multiples_list)):
        unique_combinations.update(set(itertools.combinations(prime_multiples_list,i)))
        combinations_product = list(functools.reduce(operator.mul,i) for i in unique_combinations)
        combinations_product.sort()
    try:
        return combinations_product
    except:
        return []

abundentNums = []

for n in range(1, 28123):
    if sum(calculate_divisors(n)) + 1 > n:
        abundentNums.append(n)

sums = [0] * 28124
for x in range(0, len(abundentNums)):
    for y in range(x, len(abundentNums)):
        sumOf2AbundantNums = abundentNums[x] + abundentNums[y]
        if (sumOf2AbundantNums <= 28123):
            if (sums[sumOf2AbundantNums] == 0):
                sums[sumOf2AbundantNums] = sumOf2AbundantNums

ans = 0
for i in range(1, len(sums)):
    if sums[i] == 0:
        ans += i

print(ans)

