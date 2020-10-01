import itertools

a,b = 1,0
for i in itertools.count():
	if len(str(b)) == 1000:
		print(i)
		break
	a, b = b, a + b
