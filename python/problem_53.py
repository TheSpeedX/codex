'''
Project Euler Problem 53
visit for more details - https://projecteuler.net/problem=53

Ans- 4075
'''
import math

MAX = 1000000
count = 0

for n in range(1,101):
	for r in range(1,n+1):

		C = math.factorial(n)/ ( math.factorial(r)*math.factorial(n-r) )

		if C > MAX:
			count += 1
print(count)
