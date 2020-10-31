import eulerlib

def compute():
	isprime = eulerlib.list_primality(999999)
	def is_circular_prime(n):
		s = str(n)
		return all(isprime[int(s[i : ] + s[ : i])] for i in range(len(s)))
	
	ans = sum(1
		for i in range(len(isprime))
		if is_circular_prime(i))
	return str(ans)


print(compute())
