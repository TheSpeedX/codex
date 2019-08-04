#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

num=600851475143
pf = 1
i = 2
while i <= num / i:
	if num % i == 0:
		pf = i
		num /= i
	else:
		i += 1

	if pf < num:
		pf = num
print('Largest Prime: ',int(pf))
