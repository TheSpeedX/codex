#
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math

res = 2520
for i in range(11, 21):
	res *= int(i / math.gcd(i, res))
print('LCM is ',res)
