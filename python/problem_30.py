def solution():
	return sum(i for i in range(2, 1000000) if i == sum(int(_)**5 for _ in str(i)))

print(solution())
