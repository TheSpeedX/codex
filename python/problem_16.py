a = 2
p = 1000
sum_of_digit = 0
for n in range(1,p):
    a*=2
#print(a)
count = 0
while a != 0: 
    sum_of_digit += a%10
    a //= 10
print(sum_of_digit)    
