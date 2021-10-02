#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

big=0
x,y=0,0
i=999
while i>900:
	j=999
	while j>900:
		m=i*j
		if m>big:
			if str(m)==str(m)[ : :-1]:
				big=m
				x,y=i,j
				print(str(x) +' X '+ str(y) +' = '+str(big))
				exit()
		j-=1
	i-=1
