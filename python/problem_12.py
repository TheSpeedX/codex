def sumOfNos(n):
	return sum([i for i in range(1, n+1)])

def factorCount(n):
	'''
	To find the count of factors of the number using the prime factorization of the number
	'''
	d = {}
	for i in primes:
		if n%i == 0:
			c = 0
			while n%i == 0:
				c+=1
				n = n//i
			d[i] = c
		if n <= i:
			break
	t = 1
	for i in d.values():
		t *= (i+1)
	return t

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
i=1
while True:
	if factorCount(sumOfNos(i)) >= 500:
		print(sumOfNos(i))
		break
	i+=1
