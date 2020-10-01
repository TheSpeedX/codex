#Power digit sum
#if  2 to the power 10 is 1024 and the sum of 1,0,2,4 is 7
#then mention the sum of 2 to the power 1000

n = int(input('Mention the number'))
power = int(input('Mention the power'))


def calc(n,power):
  mul = pow(n,power)
  a = str(mul)
  print(mul)
  k = list(map(int,a.strip()))
  
  return sum(k)
  
print(calc(n,power))
