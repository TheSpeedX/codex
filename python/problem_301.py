def compute():
	a = 0
	b = 1
	for i in range(32):
		a, b = b, a + b
	return str(a)


if __name__ == "__main__":
	print(compute())
